class Airplane:

    name = ''

    def __init__(self, type, year, role, country, max_speed):
        self.year = year
        self.type = type
        self.role = role
        self.country = country
        self.max_speed = max_speed

airplanes = []
plane_a = Airplane('millitary aircraft', 1955, 'strategic bomber', 'USA', '800km/h')
plane_a.name = 'B-52'
airplanes.append(plane_a)
plane_b = Airplane('civilian aircraft', 2011, 'passenger airliner', 'USA','956km/h')
plane_b.name = 'Boeing-787 Dreamliner'
airplanes.append(plane_b)
plane_c = Airplane('civilian aircraft', 1976, 'passenger supersonic airliner', 'UK-France', '2179km/h')
plane_c.name = 'Concorde'
airplanes.append(plane_c)
plane_d = Airplane('millitary aircraft', 1959, 'interceptor', 'USSR', '1300km/h')
plane_d.name = 'Mig-21'
airplanes.append(plane_d)
plane_e = Airplane('civilian aircraft', 1974, 'strategic airlifter', 'USSR', '900km/h')
plane_e.name = 'Il-76'
airplanes.append(plane_e)
plane_f = Airplane('millitary aircraft', 2005, 'air superiority fighter', 'USA', '2410km/h')
plane_f.name= 'F-22'
airplanes.append(plane_f)

for airplane in airplanes:
    print(airplane.name,':', airplane.type, '. Introduced in', airplane.year, '.', 'Role:', airplane.role, '. Produced by', airplane.country, '. Maximum speed:', airplane.max_speed, '.')



