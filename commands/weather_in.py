weather in|temperature in
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
    talkToMe("Either I do not know that city, or you are an idiot")
