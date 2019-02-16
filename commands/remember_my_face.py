remember my face

# this is facial recognition

# remove old picture
os.chdir('..')

picture_name = 'faces/' + os.listdir('faces')[0]
os.system('rm ' + picture_name)

talkToMe('What is your name?')
name = speechToText()
new_file = 'faces/' + name + '.png'

# take a picture of the person and store in the file
talkToMe(f'learning {name}s face...')
take_picture(new_file)

# go back into commands
os.chdir('commands')

'''
known_image = face_recognition.load_image_file("biden.jpg")
unknown_image = face_recognition.load_image_file("unknown.jpg")

biden_encoding = face_recognition.face_encodings(known_image)[0]
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
'''
