email
talkToMe('Who is the recipient?')
recipient = speechToText()

# strip white spaces and change 'at' to @
arrR = recipient.split(' ')
for i in range(len(arrR)):
    if arrR[i] == 'at':
        arrR[i] = "@"

recipient = ''.join(arrR)


print('Recipient: ' + recipient)




# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login(gmail_user, gmail_password)


talkToMe('What would to like to say?')
# message to be sent
message = speechToText()



talkToMe('Okay, sending email')
# sending the mail
s.sendmail(gmail_user, recipient, message)


# terminating the session
s.quit()
