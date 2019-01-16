import pickle

colors = {1: 'yellow', 2: 'red', 3: 'black', 4: 'green'}

with open('C:/Users/Mailz/PycharmProjects/GitProject/ematsyk/111.txt', 'wb') as f:
    pickle.dump(colors, f)