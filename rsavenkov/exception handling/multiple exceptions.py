def func(arg1, arg2):
    print(arg1, arg3)

try:
    func(1)
    func1(2)
except (TypeError, NameError) as e:
    print(e)