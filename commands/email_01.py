email
talkToMe('Who is the recipient?')
recipient = speechToText()

gmail_user = "blharbour2@gmail.com"
gmail_password = "Jones130"
email_user = ""

# strip white spaces and change 'at' to @
arrR = recipient.split(' ')
for i in range(len(arrR)):
    if arrR[i] == 'at':
        arrR[i] = "@"

recipient = ''.join(arrR)


print('Recipient: ' + recipient)


try:

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(gmail_user, gmail_password)

    talkToMe('What is the subject?')
    #subject of email_user
    SUBJECT = speechToText()


    talkToMe('What would to like to say?')
    # message to be sent
    TEXT = speechToText()
    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)



    talkToMe('Okay, sending email')
    # sending the mail
    s.sendmail(email_user, recipient, message)


    # terminating the session
    s.quit()

except:
    talkToMe('failed to send email')
