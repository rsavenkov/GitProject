def decorator(res):
    def ress(fn):
        def fnd(name):
            a = '_' + fn(name) + '_'
            a += '\n' + res
            return a
        return fnd
    return ress
@decorator('Programmist ')
def funcshon(name):
    return "hello " + name
s = input('add name : ')
print(funcshon(s))