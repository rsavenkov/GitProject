from f_price import fprice


class Orders:
    def __init__(self, namepizza, sise, weight):
        self.namepizza = namepizza
        self.sise = sise
        self.weight = weight

    def price(self, pizza, sise, weight):
        assert isinstance(pizza, object)
        price(pizza, sise, weight)


pizzas = []
namepizzas = []
flag = True
while flag:
    question = input("Do You want to oder pizza?  (yes / no) -   ")
    if question == 'yes':
        namepizza = input("What pizza do You want: Маргарита, Паперони, Гавайская? -   ")
        pizza = dict()
        sise = input("What sise do You like: 26, 32, 40 ? - ")
        pizza['sise'] = sise
        weight = input("What weight do You like: " + "normal" + " or " + "thin" + " ? - ")
        pizza['weight'] = weight
        price = fprice(pizza, sise, weight)
        pizza['price'] = price
        pizzas.append(pizza)
        namepizzas.append(namepizza)
        print(namepizzas)
        print(namepizza, ' = ', pizza)
        print(pizzas)
    else:
        flag = False
        break
    print(namepizza, sise, weight, price)

