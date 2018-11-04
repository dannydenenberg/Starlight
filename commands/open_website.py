open website
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
