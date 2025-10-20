# Blind_SQL_Injection_DVWA

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

-----
### Step 6
  Configure Proxy for Burp Suite to work. 
  First open the BurpSuite tool and do the following steps that captured below.
<p align="center"><img width="500" height="200" alt="image" src="https://github.com/user-attachments/assets/8e5ef056-1275-46af-8442-a531a81dadf0" /></p>

### Step 7
  Then head to `Settings` within Burp and do the following configurations.
<p align="center"><img width="500" height="350" alt="image" src="https://github.com/user-attachments/assets/acbe0ef8-d41a-404f-8226-53fb706a9329" /> </p>

### Step 8
  In the meantime locally add the proxy as listed bellow, via `Settings` on the `Network` tab. 
<p align="center"><img width="350" height="200" alt="image" src="https://github.com/user-attachments/assets/5463867f-ceb2-45d6-9e73-a1b198fe479d" /> </p>

### Step 9
  Finally we need to configure the extension called `Foxy Proxy` <br>
 [Click](https://addons.mozilla.org/en-US/firefox/addon/foxyproxy-basic/) to  add the extension. <br>
 Then add the following configurations.
<p align="center"><img width="500" height="240" alt="image" src="https://github.com/user-attachments/assets/0275b518-ba4b-4fb3-ae63-a46d9abaf0e2" /> </p>

  Lastly, do not forget to turn on the proxy!
<p align="center"><img width="170" height="160" alt="image" src="https://github.com/user-attachments/assets/781dc200-16f4-4462-8307-bade22419053" /></p>

-----

### Step 10
  Now we are ready to initiate some logs. Back to our DVWA site on the `SQL Injection (Blind)` tab we submit any type of value, our goal is just to see the log.

  Since I submited the value 1, I have respected query, within the id hold the value 1. bY following the steps depicted within the picture, we have sent our log to the repeater tab in Burp. There will be able to forward and modify the request.
  <p align="center"><img width="500" height="360" alt="image" src="https://github.com/user-attachments/assets/b1c574c7-7a23-40d7-a1a3-26196d7f5641" /></p>

  ### Step 11
  This is the part where we experiement with our SQL injection queries. <br>
  Now it is important to state that certain information are know in order to run the query.<br>
  We know about: <br>
  1. The table named `users`, where users of the website are stored.
  2. At least two columns within the `users` table exist called `user_id` and `password`
  3. The passwords are in a hashed, meaning they are written in hex.
<br>
  Therefore the query I have used is the following:

  `' OR (SELECT password FROM users WHERE user_id = 1) LIKE 'A%';#`<br>
  
  It basically asks the server whether the user with ID being equal to 1 (which we know exists), their password begins with A, A was of course a random selection out of the 16 hex characters.<br>

  We are not interested for know to necesserally get a positive answer from the server, we are just crafting the query for know.
  <p align="center"><img width="500" height="400" alt="image" src="https://github.com/user-attachments/assets/0736f25e-0682-48be-a4ec-e2a9eb16e469" /></p>

Looking the screenshot above, the response is negative meaning that the password does not start with A.<br>
We could manually of course try all the 16 possibilities... if we are mad enough!<br>

OR<br>
We could utilize the Intruder function of Burp, <br>
OR<br>
Make our own homemade python script!

## Script Running
  To run the script run the following command
  ```
  python3 sc2.py
  ```
