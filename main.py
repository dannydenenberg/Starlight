from gtts import gTTS
import speech_recognition as sr
import os
import re
import webbrowser
import smtplib
import requests
from weather import Weather
#import urllib
#import urllib2
import sys
from time import ctime

# be able to email
import smtplib
import importlib


gmail_user = "dannydenenberg@gmail.com"
gmail_password = ""

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

# IMPORTANT GMAIL ACCOUNT ID's

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

    # Saving the converted audio in a mp3 file named
    # welcome
    myobj.save("welcome1.mp3")

    # Playing the converted file
    os.system("mpg123 welcome1.mp3")
    os.system("rm welcome1.mp3")



def myCommand():
    "listens for commands"

    try:
        command = speechToText().lower()
        #if 'starlight' in command:
        print('You said: ' + command + '\n')

        if 'starlight' in command:
            assistant(command)
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')

    myCommand()



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
