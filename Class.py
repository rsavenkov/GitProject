class Table:

    label = ''

    def __init__(self, high, color):
        self.high = high
        self.color = color

tables = []

ikea = Table(90, 'black')
ikea.label = 'Ikea'
tables.append(ikea)
obi = Table(70, 'yellow')
obi.label = 'OBI'
tables.append(obi)
ashan = Table(50, 'red')
ashan.label = 'Ashan'
tables.append(ashan)

for table in tables:
    print(table.label, table.high, table.color)
