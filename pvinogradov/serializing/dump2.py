import pickle


class MyClass:

    def __init__(self, attr):
        self.attr = attr

    attr = 'Class attribute'


with open('C:/svn/untitled1/trunk/pvinogradov/serializing/hello.txt' 'wb') as f:
    pickle.dump(MyClass, f)

with open('C:/svn/untitled1/trunk/pvinogradov/serializing/hello.txt', 'rb') as f:
    my_class = pickle.load(f)
    print(my_class.attr)

my_obj = MyClass('Object attribute')

with open('C:/svn/untitled1/trunk/pvinogradov/serializing/hello1.txt', 'wb') as f:
    pickle.dump(my_obj, f)

with open('C:/svn/untitled1/trunk/pvinogradov/serializing/hello1.txt', 'rb') as f:
    my_obj = pickle.load(f)
    print(my_obj.attr)
