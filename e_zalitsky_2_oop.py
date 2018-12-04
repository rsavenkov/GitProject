
class MotoTechnic:
    firm = ''

    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.salon = "Moto-Land"

    def specifications(self, weight, top_speed, type_class):
        self.weight = weight
        self.top_speed = top_speed
        self.type_of_class = type_class


firms = []

ducati = MotoTechnic("Monster", 2004)
ducati.specifications(143, 234, "Naked")
ducati.firm = "Ducati"
firms.append(ducati)

harleydavidson = MotoTechnic("Iron 883", 2017)
harleydavidson.specifications(182, 170, "Classic")
harleydavidson.firm = "Harley-Davidson"
firms.append(harleydavidson)

honda = MotoTechnic("CBR1000RR", 2016)
honda.specifications(160, 300, "Sport")
honda.firm = "Honda"
firms.append(honda)

kawasaki = MotoTechnic("KLX", 2005)
kawasaki.specifications(115, 140, "Cross")
kawasaki.firm = "Kawasaki"
firms.append(kawasaki)

yamaha = MotoTechnic("Tenere", 1992)
yamaha.specifications(150, 165, "Tour Enduro")
yamaha.firm = "Yamaha"
firms.append(yamaha)

suzuki = MotoTechnic("DLV-Storm", 2015)
suzuki.specifications(170, 180, "Tourist")
suzuki.firm = "Suzuki"
firms.append(suzuki)

for firms in firms:
    print("=" * 85)
    print("[Salon :>", firms.salon, "][ Firm :>", firms.firm, "][ Model :>",
          firms.model, "][ Year :>", firms.year, "]")
    print("[Weight of model:>", firms.weight, "][ Top Speed :>", firms.top_speed, "][ Class :>",
          firms.type_of_class, "]")
    print("=" * 85)
