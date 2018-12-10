from math import pow

x = input('Ваше число будет возведено в степеь 2:')

try:
    print('В блоке try начало')
    print(pow(x, 2))
    print('В блоке try конец')
except TypeError as e:
    print('В блоке except', e)
    x = int(x)
    print(pow(x, 2))    # обработать ValueError
else:
    print('Блок else, в том случае если исключение не вызвано') # необходимо попасть в этот блок