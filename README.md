# Blind_SQL_Injection_DVWA-

## Brief Description

## Script Running

### Step 1
  Run the DVWA docker through terminal
  ```
  sudo docker run --rm -it -p 80:80 vulnerables/web-dvwwa
  ```
### Step 2
  Open the browser enter `http://localhost/login.php`

### Step 3
  Now enter credentials for Username: `admin` Password: `password`

<p align="center"><img width="240" height="240" alt="image" src="https://github.com/user-attachments/assets/9c6c1812-427c-4518-a57e-7196e2843844" /></p>

### Step 4
  Click on  `Create / Reset Database`
<p align="center"><img width="650" height="200" alt="image" src="https://github.com/user-attachments/assets/b83ad2b3-9b5a-4755-9e3e-47fb6bd7b9c3" /></p>

### Step 5
  Head to `SQL Injection (Blind)` tab
<p align="center"><img width="600" height="325" alt="image" src="https://github.com/user-attachments/assets/38f2f475-2b76-41e5-8c3d-6e5653cbd1cd" /> </p>

  By default website can only return two options, without any further data being displayed, based whether the User exists or not as stated.
| Option A | Option B | 
| :------------------: | :----------: |
| <img width="500" height="280" alt="image" src="https://github.com/user-attachments/assets/5df58529-73e3-4d91-bb7f-8ca7059918bd" />  | <img width="500" height="280" alt="image" src="https://github.com/user-attachments/assets/fab242b8-f33e-4102-bc1c-76470dda3d86" />  | 

### Step 6
  Configure Proxy for Burp Suite to work
<p align="center"></p>

## Script Running
  To run the script run the following command
  ```
  python3 sc2.py
  ```
