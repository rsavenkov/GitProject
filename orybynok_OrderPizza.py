from f_price import price
class Orders:
    def __init__(self, pizza, sise, weight):
        self.pizza = pizza
        self.sise = sise
        self.weight = weight
    def price(self,pizza, sise, weight):
        price(pizza, sise, weight,)

pizza = input("What pizza do You want: Маргарита, Паперони, Гавайская? -   ")
sise = input("What sise do You like: 26, 32, 40 ? - ")
weight = input("What weight do You like: "+"normal"+" or "+"thin"+" ? - ")
print(pizza,sise,weight)
price(pizza,sise,weight)


