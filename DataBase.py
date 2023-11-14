import requests

from bs4 import BeautifulSoup

import sqlite3

from datetime import datetime



conn = sqlite3.connect('weather.db')

c = conn.cursor()



c.execute('''CREATE TABLE IF NOT EXISTS weather

            (date_time text, temperature real)''')



url = 'https://www.meteoprog.ua/ua/weather/Kyiv/'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

temperature = soup.find('span', class_='temp').get_text()



now = datetime.now()

date_time = now.strftime("%Y-%m-%d %H:%M:%S")

c.execute("INSERT INTO weather (date_time, temperature) VALUES (?, ?)", (date_time, temperature))

conn.commit()


conn.close()