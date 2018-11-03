
# Python code to illustrate Sending mail from
# your Gmail account
import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("dannydenenberg@gmail.com", "wag%%qiyimaccentral269")

# message to be sent
message = "Hey, dude. \nThis is starlite....hit me up!"

# sending the mail
s.sendmail("dannydenenberg@gmail.com", "blharbour9@gmail.com", message)

# terminating the session
s.quit()
