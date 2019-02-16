youtube play
search_index = command.find('play') + 1;
search = command[search_index:]
base = "https://www.youtube.com/results?search_query="
qstring = (search)

r = requests.get(base+qstring)

page = r.text
soup=bs(page,'html.parser')

vids = soup.findAll('a',attrs={'class':'yt-uix-tile-link'})

videolist=[]
for v in vids:
    tmp = 'https://www.youtube.com' + v['href']
    videolist.append(tmp)

webbrowser.open(tmp)
