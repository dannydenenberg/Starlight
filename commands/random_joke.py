joke|jokes

res = requests.get(
        'https://icanhazdadjoke.com/',
        headers={"Accept":"application/json"}
        )
if res.status_code == requests.codes.ok:
    talkToMe(str(res.json()['joke']))
else:
    talkToMe('oops!I ran out of jokes')
