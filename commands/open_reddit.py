open reddit
reg_ex = re.search('open reddit (.*)', command)
url = 'https://www.reddit.com/'
if reg_ex:
    subreddit = reg_ex.group(1)
    url = url + 'r/' + subreddit
webbrowser.open(url)
print('Done!')
