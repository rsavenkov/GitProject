from r_klimenko_truck import Track

class MiniTraktor(Track):

    brend = 'cat'
    country = ''

    def __init__(self, model, color, age):
        super(). __init__(Track.country, Track.marketinglevel)
        self.model = model
        self.color = color
        self.age = age

a = MiniTraktor('1x','black', 5)

l = []
l.append(a)
print(l[0])






