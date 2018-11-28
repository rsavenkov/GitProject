from functools import reduce
lis = [1,2,3,4,5,6,7,8,9,10]
a = reduce(lambda a, b: a if a > b else b , lis)
print(a)