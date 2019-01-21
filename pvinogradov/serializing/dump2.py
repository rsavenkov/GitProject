import pickle


class MyClass:

    def __init__(self, attr, attr1):
        self.attr = attr
        self.attr1 = attr1

    attr11 = 'Class attribute'


with open('C:/svn/untitled1/trunk/pvinogradov/serializing/12.txt', 'wb') as f:
    pickle.dump(MyClass, f)

with open('C:/svn/untitled1/trunk/pvinogradov/serializing/12.txt', 'rb') as f:
    my_class = pickle.load(f)
    print(my_class.attr11)

my_obj = MyClass('Object attribute', 123)

with open('C:/svn/untitled1/trunk/pvinogradov/serializing/12.py', 'wb') as f:
    pickle.dump(my_obj, f)

with open('C:/svn/untitled1/trunk/pvinogradov/serializing/12.py', 'rb') as f:
    my_obj = pickle.load(f)
    print(my_obj.attr,my_obj.attr)
    print(my_obj.attr1)
