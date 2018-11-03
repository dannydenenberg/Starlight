import smtplib

# set up credentials
gmail_user = 'dannydenenberg@gmail.com'
gmail_password = 'wag%%qiyimaccentral269'

# set up email body
sent_from = 'dannydenenberg@gmail.com'
to = ['dannydenenberg@gmail.com', 'dannydanielod@gmail.com']
subject = 'OMG Super Important Message'
body = 'Hey, what\'s up?\n\n--Starlite test'

# HERE is the full body
email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

# UNCOMMENT
'''
try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print('Email sent!')
except:
    print('Something went wrong...')
'''


server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(gmail_user, gmail_password)
server.sendmail(sent_from, to, email_text)
server.close()
