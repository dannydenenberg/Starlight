google search
search_index = command.find('google search') + len('google search') + 1;
search = command[search_index:]

url = "https://www.google.com/search?q=" + search
webbrowser.open(url)
