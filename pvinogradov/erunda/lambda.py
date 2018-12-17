def fn(start, end, fn):
    n = 0
    for i in range(start, end + 1):
        n += fn(i)
    return n


def siruia(x):
    return x ** 2


print(fn(1, 10, siruia))
print(fn(1, 10, lambda n: n * 83))
