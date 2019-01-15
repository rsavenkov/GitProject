from timeit import Timer


def sum_one(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum


def sum_two(n):
    sum = (n * (n + 1) / 2)
    return sum


t = Timer("sum_two(100000)", "from __main__ import sum_two")
r = Timer("sum_one(100000)", "from __main__ import sum_one")

print('{0:.6f}'.format(t.timeit(number=1)))
print('{0:.6f}'.format(r.timeit(number=1)))

# a = sum_one(10)
# b = sum_two(10)
# print(a)
# print(b)
