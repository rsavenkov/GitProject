from f_credit import credit
from f_ank_deb import f_ank_deb

bory = {'gender': True, 'age': 30, 'status': 'single', 'status1': 'jobless'}
donat = {'gender': True, 'age': 35, 'status': 'married', 'status1': 'work'}
valy = {'gender': False, 'age': 34, 'status': 'married', 'status1': 'work'}
lyly = {'gender': False, 'age': 37, 'status': 'married', 'status1': 'jobless'}
nady = {'gender': False, 'age': 27, 'status': 'single', 'status1': 'work'}
katy = {'gender': False, 'age': 23, 'status': 'single', 'status1': 'jobless'}
names = [bory, donat, valy, lyly, nady, katy]
flag = True
while flag:
    question = input("\nВы хотите получить кредит? - ( да \ нет )   ")
    if question == 'да':
        name = input("\nДавайте заполним анкету.\n Ваше имя? -   ")
        name = {}
        gender = input("Вы мужчина или женщина? Ответьте: ( True \ False )   ")
        name['gender'] = gender
        age = int(input("Ваш возраст?  -   "))
        name['age'] = age
        status = input("Вы состоите в браке? Ответьте:   ( single \ married )   ")
        name['status'] = status
        status1 = input("Вы работаете? Ответьте :   ( work \ jobless )   ")
        name['status1'] = status1
        print("\n")
        names.append(name)
    for name in names:
        print("\n")
        f_ank_deb(name)
        print('\nРешение по кредиту:')
        credit(name['gender'],name['age'],name['status'],name['status1'])
    else:
        break

