weather forecast in
reg_ex = re.search('weather forecast in (.*)', command)

try:
    if reg_ex:
        city = reg_ex.group(1)
        weather = Weather()
        location = weather.lookup_by_location(city)
        forecasts = location.forecast

        for i in range(0,1):
            talkToMe('''On %s will it %s. The maximum temperture will be %.1f degrees.\n
            The lowest temperature will be %.1f degrees.''' %
            (forecasts[i].date, forecasts[i].text, int(celToFah(forecasts[i].high)), int(celToFah(forecasts[i].low))))
except:
    talkToMe('I am sorry. I do not know that city.')
