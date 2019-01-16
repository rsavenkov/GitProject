 import pickle

class AddData:

    diction = { 1 : ["fsfs", "fsf", [3213, 3333], 222],
                2 : ("WFWEFW", "WFWFWF"),
                3 : "dfwfwfwfwvcvc",
                4 : {1 : 2222, 2 : 45321}
    }

    def __init__(self, addit):
         self.addit = addit

    def addit(self):
         AddData.addit(AddData.diction.update(self.addit))

with open(r'C:\Users\Xiaomi\Documents\Exploit_directories\Python\PycharmProjects\GitProject\ezalitsky\different\serialisation\11.pickle', 'wb') as d:
    pickle.dump(AddData, d)

with open(r'C:\Users\Xiaomi\Documents\Exploit_directories\Python\PycharmProjects\GitProject\ezalitsky\different\serialisation\11.pickle', 'rb') as d:
    my_class = pickle.load(d)
    print("clear ", my_class.diction)

datan = AddData({"new": "new data"})

with open(r'C:\Users\Xiaomi\Documents\Exploit_directories\Python\PycharmProjects\GitProject\ezalitsky\different\serialisation\11.pickle', 'wb') as d:
    pickle.dump(datan, d)

with open(r'C:\Users\Xiaomi\Documents\Exploit_directories\Python\PycharmProjects\GitProject\ezalitsky\different\serialisation\11.pickle', 'rb') as d:
    datan = pickle.load(d)
    print("after additing", datan.diction)