
# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os

def talkToMeNew(myText):

    # Language in which you want to convert
    language = 'en'

    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells
    # the module that the converted audio should
    # have a high speed
    myobj = gTTS(text=myText, lang=language, slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome
    myobj.save("welcome1.mp3")

    # Playing the converted file
    os.system("mpg123 welcome1.mp3")
    os.system("rm welcome1.mp3")

talkToMeNew('Hello. How are you today?')
