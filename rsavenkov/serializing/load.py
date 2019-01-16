import pickle

with open('C:/Users/Mailz/PycharmProjects/GitProject/rsavenkov/serializing', 'rb') as f:
    colors = pickle.load(f)
    print(colors[1])