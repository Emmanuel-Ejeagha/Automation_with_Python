# Weather forecast

import requests

def get_weather(city, units='metric', api_key='078734d940b4d7053c436b956a1a7a0d'):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}"
    r = requests.get(url)
    content = r.json()
    datas = content['list']
    with open('RESTFUL_API/data.txt', 'a') as file:
        for data in datas:
            file.write(f"{data['dt_txt']}, {data['main']['temp']}, {data['weather'][0]['description']}\n")

print(get_weather(city='Lagos'))