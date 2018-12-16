from car import Carall



class datsun(Carall):

    def __init__(self, color, distatnce, owner):
        super().__init__("Datsun", "Undo", "sedan")
        self.color = color
        self.distance = distatnce
        self.owner = owner

    def fullinfo(self):
        return super().fullinf() + "Color = {}\nDistance = {}\nOwner = {}\n" \
            .format(self.color, self.distance, self.owner) + "=============================\n"

class hundai(Carall):

    def __init__(self, color, distance, owner):
        super().__init__("Hundai", "Tucson", "jeep")
        self.color = color
        self.distance = distance
        self.owner = owner

    def fullinfo(self):
        return super().fullinf() + "Color = {}\nDistance [ml] = {}\nOwner = {}\n" \
            .format(self.color, self.distance, self.owner) + "=============================\n"

type_car = []

type_car1 = datsun("Green", 12300, "Below Nikolay")
type_car.append(type_car1)
print("Auto 1 : " + type_car1.fullinfo())
type_car2 = hundai("Green", 12300, "Zaicev Oleg")
type_car.append(type_car2)
print("Auto 2 : " + type_car2.fullinfo())
type_car3 = datsun("Green", 12300, "Ivanov Ilya")
type_car.append(type_car3)
print("Auto 3 : " + type_car3.fullinfo())
type_car4 = hundai("Green", 12300, "Carev Mihail")
type_car.append(type_car4)
print("Auto 4 : " + type_car4.fullinfo())
