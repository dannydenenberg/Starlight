# google text to speech; extremely important for the speech to text function
from gtts import gTTS

# for plaing youtube video
from bs4 import BeautifulSoup as bs

# important for facial recognition
import face_recognition

# speech to text
import speech_recognition as sr

#interact with the os' operating system
import os

# regular expressions
import re

# allows the python to open a window on the default browser and search something
import webbrowser

# be able to email
import smtplib

# GET, PUT, etc. send request to server --> recieve code; used in the jokes file in commands
import requests

# used to request weather; another possibility is to use the requests module for a site, which I think is entirely possible, but this works too
#from weather import Weather

# interacts with the operating system as does `os`; you can exit a program as well
import sys

# gets the entire date; month, day, year, hours, minutes, seconds
import time



# for facial recognition
def take_picture(path):
    import time
    import cv2
    camera_port = 0
    camera = cv2.VideoCapture(camera_port)
    time.sleep(0.1)  # If you don't wait, the image will be dark
    return_value, image = camera.read()
    cv2.imwrite(path, image)
    del(camera)  # so that others can use the camera as soon as possible

# compares a picture taken now to the one stored in 'faces'
def who_am_i():
    print("starting whoami:")
    pic_path = '../faces/' + os.listdir('../faces')[0]
    print(f'pic path = {pic_path}')

    take_picture('test.png')

    known_image = face_recognition.load_image_file(pic_path)
    unknown_image = face_recognition.load_image_file("test.png")

    print('starting encodings')
    person_encoding = face_recognition.face_encodings(known_image)[0]
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

    print('making results')
    results = face_recognition.compare_faces([person_encoding], unknown_encoding)

    print('deleting test.png')
    os.system('rm test.png')

    # if there are no faces in the image, then there will be no true or false values in the array, it will just be []

    print('returning results')
    return results

# All this does is converts speech to text
def speechToText():
    # get audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source)
        return r.recognize_google(audio)


def celToFah(c):
    return (c * (9.0/5)) + 32



## NOTE: Add extra print statements in here if the Pi's sound output is not working
def talkToMe(text):
    "speaks audio passed as argument"

    print(text)
    # Language in which you want to convert
    language = 'en'

    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells
    # the module that the converted audio should
    # have a high speed
    myobj = gTTS(text=text, lang=language, slow=False)

    # Saving the converted audio in a mp3 file named `x.mp3`
    myobj.save("x.mp3")

    # Playing the converted file
    os.system("mpg321 x.mp3")
    os.system("rm x.mp3")


# where the text said is taken and used
def myCommand():
    "listens for commands"

    try:
        command = speechToText().lower()

        #if 'starlight' in command:
        print('You said: ' + command + '\n')

        if 'starlight' in command:
            try:
                # talkToMe('You said starlight! Yay!')
                assistant(command)
            except Exception as e:
                talkToMe('Something went wrong.')
                print(e)
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')





## Handles all of the commands
def assistant(command):
    os.chdir('commands')

    for file_n in os.listdir():
        with open(file_n) as file:
            contents = file.read()
            com = contents[:contents.find('\n')].split('|') # what is the command to search for in what the person said: you can add multiple commands by separating them with pipes (|)
            for com_specific in com:
                if com_specific in command:
                    exec(contents[contents.find('\n'):]) # execute the code directly under the command to search for
                    break

    os.chdir('..') # go back to root





def read_file(file):
    with open(file, 'r') as myfile:
        return myfile.read()


talkToMe('I am ready for your command')


#loop to continue executing multiple commands
while True:
    myCommand()
