# стандартный калькулятор
def sum(a, b):
    res = a + b
    return res

def multip(a, b):
    res = a * b
    return res

def delit(a, b):
    res = a / b
    return res


def default():
    return 'incorrect input'


switcher = {
    1: sum,
    2: multip,
    3: delit,
    4: default
}


def switch(operation):
    return switcher.get(operation)


print('Programma dlya vichisleniy')
vvod = input('VVedite что хотите сделать :\n 1 : +\n 2 : *\n 3 : / \nVash vibor :')
vvod = int(vvod)
if vvod == 1 or vvod == 2 or vvod == 3:
    a = float(input("Vvedite pervoe chislo :"))
    b = float(input("Vvedite vtoroe chislo :"))
    print(switch(vvod)(a, b))
elif vvod == 4:
    print(switch(4))
else:
    print("Your vvod incorrect")
