import csv
import json

import requests
import pyquery
cities = ["Москва", "Санкт-Петербург", "Новосибирск", "Екатеринбург", "Нижний Новгород", "Казань", "Челябинск", "Омск",
          "Самара",
          "Ростов-на-Дону", "Уфа", "Красноярск", "Воронеж", "Пермь", "Волгоград", "Краснодар", "Саратов", "Тюмень",
          "Тольятти",
          "Ижевск", "Барнаул", "Ульяновск", "Иркутск", "Хабаровск", "Ярославль", "Владивосток", "Махачкала", "Томск",
          "Оренбург",
          "Кемерово", "Новокузнецк", "Рязань", "Астрахань", "Набережные Челны", "Пенза", "Киров", "Липецк", "Чебоксары",
          "Калининград"]


def get_data(hack):
    title = hack.split('\n')[0]
    theme = hack.split('\n')[1]
    try:
        url = 'http' + hack.split('http')[1].split('\n')[0]
    except:
        url = None
    if len(hack.split('Даты')):
        date = hack.split('Даты')
        date = date[1]
        date = date.split('\n')[0]
        date.replace(':', '')
        date.strip()
    else:
        date = None

    city = None
    for c in cities:
        if c in hack:
            city = c
    if 'Онлайн' in hack:
        city = 'Онлайн'
    if title and date and city and url:
        return {
            'Название': title,
            'Темы': theme,
            'Даты': date,
            'Город': city,
            'Ссылка': url
        }
    else:
        return None

html = requests.get('http://www.xn--80aa3anexr8c.xn--p1ai/').text

pq = pyquery.PyQuery(html)

hacks = [pq(hack).text() for hack in pq('.t527__wrapperleft')]
data = [get_data(hack) for hack in hacks]
data = [i for i in data if i]


with open('hacks.json', 'w') as output_file:
    json.dump(data, output_file)
