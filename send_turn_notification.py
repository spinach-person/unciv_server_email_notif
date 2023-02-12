from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
import sys

# 1st argument is the recipient email address
recipient_address = sys.argv[1]
# 2nd argument is the name of the Unciv game
game_name = sys.argv[2]

notifyer_email_file = "./email_info/notifyer_email.json"

with open(notifyer_email_file, "rt") as file:
    json_data = json.load(file)

sender_address = json_data["address"]
sender_username = json_data["username"]
sender_password = json_data["password"]
smtp_server = json_data["smtp_server"]
smtp_port = json_data["smtp_port"]

subject = "Unciv Game Turn Reminder"
body = "It is your turn on Unciv game " + game_name

message = MIMEMultipart()
message["From"] = sender_address
message["To"] = recipient_address
message["Subject"] = subject
message.attach(MIMEText(body))

smtp = SMTP(smtp_server, smtp_port)
smtp.set_debuglevel(2)
smtp.ehlo()
smtp.starttls()
smtp.ehlo()
smtp.login(sender_username, sender_password)
smtp.sendmail(sender_address, recipient_address, message.as_string())
smtp.quit()
