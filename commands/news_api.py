news
#key: 4d12c90dacef4e69bd9c4e6ba8b6f4f7
url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=4d12c90dacef4e69bd9c4e6ba8b6f4f7')
response = requests.get(url)

# read the description of the first article with a description, then stop
#print(response.json())

talkToMe('Would you like a specific station? ')
res = speechToText().lower()
print("RES: " + res)



for i in response.json()["articles"]:
    station = i["source"]["name"].lower()
    print('station: ' + station)

    if "description" in i:
        if res != 'no' and res == station:
            print('SPECIFIC ')
            talkToMe("From " + station + i["description"])
        else:
            print('NOT ______ SPECIFIC ')
            talkToMe("From " + station + i["description"])
