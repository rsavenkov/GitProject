import pickle

with open('C:/Users/Ruslan/PycharmProjects/GitProject/trunk/rsavenkov/serializing/colors.pickle', 'rb') as f:
    colors = pickle.load(f)
    print(colors)