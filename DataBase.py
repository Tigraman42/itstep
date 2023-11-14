import sqlite3
import requests

conn = sqlite3.connect('weather.db')

c = conn.cursor()


c.execute('''CREATE TABLE IF NOT EXISTS weather

            (date_time TEXT, temperature REAL)''')


conn.commit()

conn.close()


url = 'https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D1%87%D0%B5%D1%80%D0%BA%D0%B0%D1%81%D0%B8'

response = requests.get(url)


if response.status_code == 200:

   html = response.content

else:

   print('Не вдалося отримати сторінку')


from bs4 import BeautifulSoup


soup = BeautifulSoup(html, 'html.parser')

today_weather = soup.find('div', {'class': 'weatherToday'}).find('div', {'class': 'temperature'}).text

today_temperature = int(today_weather.split('°')[0])


print(f"Температура сьогодні: {today_temperature}°C")

print(soup)


import datetime

import sqlite3


temperature = today_temperature

date_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


conn = sqlite3.connect('weather.db')

c = conn.cursor()


c.execute("INSERT INTO weather VALUES (?, ?)", (date_time, temperature))


conn.commit()

conn.close()