# Blind_SQL_Injection_DVWA

## Step 1
  In case you are planning to follow along, I would recommend to follow my intial steup guide. <br>
 [Click](https://github.com/EleniChristopoulou/DVWA_Initial_Setup-/tree/main) here to check it out.

## Step 2
  Now it is the time where we interact with site in order to discover actual functionality.<br>
  It is important to pay attention on the input and the output.<br>
  Head to `SQL Injection (Blind)` tab.
<p align="center"><img width="600" height="325" alt="image" src="https://github.com/user-attachments/assets/38f2f475-2b76-41e5-8c3d-6e5653cbd1cd" /> </p>

  By default website can only return two options, without any further data being displayed, based whether the User exists or not as stated.
| Option A | Option B | 
| :------------------: | :----------: |
| <img width="500" height="280" alt="image" src="https://github.com/user-attachments/assets/5df58529-73e3-4d91-bb7f-8ca7059918bd" />  | <img width="500" height="280" alt="image" src="https://github.com/user-attachments/assets/fab242b8-f33e-4102-bc1c-76470dda3d86" />  | 

## Step 3
  Now we are ready to initiate some logs. Back to our DVWA site on the `SQL Injection (Blind)` tab we submit any type of value, our goal is just to see the log.

  Since I submited the value 1, I receive the respected query, within the id hold the value 1. By following the steps depicted within the picture, we have sent our log to the repeater tab in Burp. There will be able to forward and modify the request.
  <p align="center"><img width="500" height="360" alt="image" src="https://github.com/user-attachments/assets/b1c574c7-7a23-40d7-a1a3-26196d7f5641" /></p>

## Step 4
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
Make our own homemade python script!<br>

To be more precise, I will make the script and you can just download it and run it, or of course make your own.<br>

However if you decide to go my way, it is really important to modify just one parameter, which is the cookie session.<br>

Don't panic is just a simple Ctrl+C Ctrl+V situation.

## Step 5
Within the Burp, simply copy the cookie session.
Then search within the python script for the cookie and replace it. Just as stated in the screenshot bellow<br>
<p align="center"><img width="1427" height="401" alt="image" src="https://github.com/user-attachments/assets/cb5889a8-f3e0-43eb-b345-190678e48a51" /></p>

Now we are ready to go!

## Step 6
  To run the script run the following command <br>
  This a slow script, the purpose is to observe and understand how the algorithm operates behind, for furtther improvement.<br>
  ```
  python3 sc2.py
  ```
Hey, do not forget to cd within the directory where you python script is! :) You are welcome.

## Step 6 (But faster)
  To run the script run the following command
  ```
 python3 sc_speed.py
  ```

https://github.com/user-attachments/assets/94d40bf2-b7be-442f-886f-bc643261805d
















