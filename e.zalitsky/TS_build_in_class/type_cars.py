from car import Car_all


class car_datsun(Car_all):

    def __init__(self, color, distatnce, owner):
        super().__init__("Datsun", "Undo", "sedan")
        self.color = color
        self.distance = distatnce
        self.owner = owner

    def fullinfo(self):
        return super().fullinf() + "Color = {}\nDistance = {}\nOwner = {}\n" \
            .format(self.color, self.distance, self.owner) + "=============================\n"

class car_hundai(Car_all):

    def __init__(self, color, distance, owner):
        super().__init__("Hundai", "Tucson", "jeep")
        self.color = color
        self.distance = distance
        self.owner = owner

    def fullinfo(self):
        return super().fullinf() + "Color = {}\nDistance [ml] = {}\nOwner = {}\n" \
            .format(self.color, self.distance, self.owner) + "=============================\n"

type_car = []

type_car1 = car_datsun("Green", 12300, "Below Nikolay")
type_car.append(type_car1)
print("Auto 1 : " + type_car1.fullinfo())
type_car2 = car_hundai("Green", 12300, "Zaicev Oleg")
type_car.append(type_car2)
print("Auto 2 : " + type_car2.fullinfo())
type_car3 = car_datsun("Green", 12300, "Ivanov Ilya")
type_car.append(type_car3)
print("Auto 3 : " + type_car3.fullinfo())
type_car4 = car_hundai("Green", 12300, "Carev Mihail")
type_car.append(type_car4)
print("Auto 4 : " + type_car4.fullinfo())
