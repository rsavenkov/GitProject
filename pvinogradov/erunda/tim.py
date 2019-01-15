def one(a):
    res = 0
    for i in a:
        for o in a:
            res += i * o
    return res


a = one(2, 3)
print(a)
