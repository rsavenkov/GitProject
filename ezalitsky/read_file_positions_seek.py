with open("C:/Users/Xiaomi/Documents/Exploit_directories/Python/PycharmProjects/itmonopoly/ezalitsky/text_RUN", "r+")\
        as f:


# 0123456789abcdef

# у seek  есть 3 аргумента откуда 0 - начало(можно опускать), 1 - с текущей позиции, 2 - с конца

    f.seek(3)
    data = f.read(3)
    print(data)

    f.seek(2, 1)
    data = f.read(3)
    print(data)

    f.seek(-3, 2)
    data = f.read(2)
    print(data)
