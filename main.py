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

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Ready...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()

        if 'starlight' in command:
            print('You said: ' + command + '\n')
            assistant(command)

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        myCommand()

def assistant(command):
    "if statements for executing commands"
    if 'open reddit' in command:
        reg_ex = re.search('open reddit (.*)', command)
        url = 'https://www.reddit.com/'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        print('Done!')

    elif 'open ' in command:
        reg_ex = re.search('open website (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain
            url = url.replace(" ", "")
            #url = url.replace("%20", "")
            webbrowser.open(url)
            print('Done!')
        else:
            pass

    elif 'what\'s up' in command:
        talkToMe('Just doing my thing')

    elif 'goodbye' in command:
        talkToMe('bye bye, I am shutting down, dear.')
        print("hello")
        sys.exit()

    elif 'joke' in command:
        res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"}
                )
        if res.status_code == requests.codes.ok:
            talkToMe(str(res.json()['joke']))
        else:
            talkToMe('oops!I ran out of jokes')

    elif 'google search' in command:
        search_index = command.find('google search') + len('google search') + 1;
        search = command[search_index:]

        url = "https://www.google.com/search?q=" + search
        webbrowser.open(url)


    elif 'youtube search' in command:
        search_index = command.find('youtube search') + len('google search') + 1;
        search = command[search_index:]
        url = "https://www.youtube.com/results?search_query=" + search
        webbrowser.open(url)

    elif 'weather in' or 'temperature in' in command:
        reg_ex = []
        reg_ex.append(re.search('weather in (.*)', command))
        reg_ex.append(re.search('temperature in (.*)', command))

        try:
            for each_reg_ex in reg_ex:
                if each_reg_ex:
                    city = each_reg_ex.group(1)
                    weather = Weather()
                    location = weather.lookup_by_location(city)
                    condition = location.condition
                    talkToMe('The Current weather in %s is %s The temperature is %.1f degrees fahrenheit' % (city, condition.text, (int(condition.temp))*1.8+32))
        except Exception as e:
            talkToMe("you are an idiot")

# ----------------------------------------------------------------------


    if 'weather forecast in' in command:
        reg_ex = re.search('weather forecast in (.*)', command)

        try:
            if reg_ex:
                city = reg_ex.group(1)
                weather = Weather()
                location = weather.lookup_by_location(city)
                forecasts = location.forecast

                for i in range(0,1):
                    talkToMe('On %s will it %s. The maximum temperture will be %.1f degrees.'
                             'The lowest temperature will be %.1f degrees.' % (forecasts[i].date, forecasts[i].text, (int(forecasts[i].high)-32)/1.8, (int(forecasts[i].low)-32)/1.8))
        except:
            talkToMe('I am sorry. I do not know that city.')


    elif 'exit program' in command:
         talkToMe('bye bye, I am shutting down dear.')
         print("hello")
         sys.exit()


    elif 'email' in command:
        talkToMe('Who is the recipient?')
        recipient = myCommand()

        if 'John' in recipient:
            talkToMe('What should I say?')
            content = myCommand()

            #init gmail SMTP
            mail = smtplib.SMTP('smtp.gmail.com', 587)

            #identify to server
            mail.ehlo()

            #encrypt session
            mail.starttls()

            #login
            mail.login('username', 'password')

            #send message
            mail.sendmail('John Fisher', 'JARVIS2.0@protonmail.com', content)

            #end mail connection
            mail.close()

            talkToMe('Email sent.')

        else:
            talkToMe('I don\'t know what you mean!')




talkToMe('I am ready for your command')

#loop to continue executing multiple commands
while True:
    myCommand()
