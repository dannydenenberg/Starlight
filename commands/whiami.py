who am i

print("IN WHO AM I > PY ")
    # if there are no faces in the image, then there will be no true or false values in the array, it will just be []

people = who_am_i()
print(f'people = {people}')

# if there is the person in the image
one_is_true = [i for i in people if i]

name = os.listdir('../faces')[0][0:-4]

# no people in the picture taken
if len(people) == 0:
    talkToMe("I don't see anyone")
elif len(one_is_true) >= 1: # there is one person in the picture and it is the right person
    talkToMe("It's " + name)
elif len(one_is_true) == 0: # there is no right person in the picture
    talkToMe('I don\'t know you')
