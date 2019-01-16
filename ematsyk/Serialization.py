import pickle
data = {
    'a': [1, 2.0, 3, 4+6j],
    'b': 124,
    'c': 'hsth'
}

with open('data.picle', 'wb') as x:
    pickle.dump(data, x)

with open ('data.picle', 'rb') as x:
    data_new = pickle.load(x)

print(data_new)