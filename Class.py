class Student:
    def __init__(self, name, surname, teacher):
        self.name = name
        self.surname = surname
        self.teacher = teacher

        
class Teacher:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.course = 'Python'


teacher = Teacher('Ruslan', 'Savenkov')
students = []
for i in range(1, 8):
    student = Student('name-' + str(i), 'name-' + str(i), teacher)
    print(student)
