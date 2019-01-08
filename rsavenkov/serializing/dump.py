import pickle

colors = {1: 'yellow', 2: 'red', 3: 'black', 4: 'green'}

with open('C:/Users/Ruslan/PycharmProjects/GitProject/trunk/rsavenkov/serializing/colors.pickle', 'wb') as f:
    pickle.dump(colors, f)