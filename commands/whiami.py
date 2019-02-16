who am i

person = who_am_i()

name = os.listdir('../faces')[0][0:-4]

if person:
    talkToMe('You are ' + name)
else:
    talkToMe("I don't know you")
