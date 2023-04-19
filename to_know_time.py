import datetime as dt

UTC_OFFSET = {
    'Санкт-Петербург': 3,
    'Москва': 3,
    'Самара': 4,
    'Новосибирск': 7,
    'Екатеринбург': 5,
    'Нижний Новгород': 3,
    'Казань': 3,
    'Челябинск': 5,
    'Омск': 6,
    'Ростов-на-Дону': 3,
    'Уфа': 5,
    'Красноярск': 7,
    'Пермь': 5,
    'Воронеж': 3,
    'Волгоград': 3,
    'Краснодар': 3,
    'Калининград': 2
}

def hello (city):
    return request (city)

def what_time(city):
    utc_time = dt.datetime.utcnow()
    city_time = dt.timedelta(hours = UTC_OFFSET[city])
    current_time = utc_time + city_time
    print (f'Текущее время в городе {city}: {current_time} (UTC + {UTC_OFFSET[city]})')
    print ('Введите город:')
    hello (input (''))

def request (city):
    if city in UTC_OFFSET.keys():
       return what_time(city)
    else:
        print ('Введите город из списка')
        request(input(''))

print('Введите название города, чтобы узнать текущее время:')
print (f'Доступные города:{list(UTC_OFFSET)}')
hello (input (''))
