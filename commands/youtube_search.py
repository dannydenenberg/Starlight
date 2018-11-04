youtube search
search_index = command.find('youtube search') + len('google search') + 1;
search = command[search_index:]
url = "https://www.youtube.com/results?search_query=" + search
webbrowser.open(url)
