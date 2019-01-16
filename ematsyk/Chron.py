class storage:
    def __init__(self, season, city, item):
        self.season = season
        self.city = city
        self.item = item

    season = ['Зима', 'Лето', 'Осень', 'Весна', 'зима', 'лето', 'осень', 'весна']
    city = ()
    item = ()

    def check_seasons(self):
        x = input('Введите время года: ')
        if x not in season:
            print('неверное время года')
v = storage()

print(v.season)