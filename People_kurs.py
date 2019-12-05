'''class Univer_People:
    def __init__(self, vtype, name, surname, birthday, facultet):
        self.vtype = vtype
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.facultet = facultet
        #self.money = money
        #self.years = years
'''
class Student:
    def __init__(self, name, surname, birthday, stipend, facultet, kusrs):
        #self.vtype = vtype
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.facultet = facultet
        self.stipend = stipend
        self.kusrs = kusrs

class Prepod:
    def __init__(self, name, surname, birthday, zp, facultet, stazh):
        #self.vtype = vtype
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.facultet = facultet
        self.zp = zp
        self.stazh = stazh

class Kontroler:
    def __init__(self, path):
        self.path = path

    def readFile(self):
        """ Метод считывания информации из файла """
        users = []
        for line in open(self.path):
            user = []
            for i in line.split(' '):
                user.append(i.split('=')[1])
            users.append(user)
        return users


    def person_list(list):
        """ Метод создания 2х отдельных списков  - студентов и преподов """
        name = 1
        surname = 2
        birthday = 3
        money = 4
        facultet = 5
        count_year = 6
        students = []
        prepods = []
        for i in list:
            if i[0] == 'студент':
                line = Student(i[1], i[2], i[3], i[4], i[5], i[6])
                students.append(line)
            elif i[0] == 'преподаватель':
                line = Prepod(i[1], i[2], i[3], i[4], i[5], i[6])
                prepods.append(line)
        return students, prepods

    def DisplayData(list):
        """ Метод вывода информации """
        print('Список всех чуваков:')
        print()
        print('%-14s' ': ' '%-10s' '%-12s' '%-17s' '%-14s' '%-11s' '%-5s' % ('Должность', 'Имя', 'Фамилия', 'Дата Рождения', 'стипендия/зп', 'Факульткет', 'Курс/Стаж'))
        print()
        for i in list:
            print('%-14s' ': ' '%-10s' '%-12s' '%-17s' '%-14s' '%-11s' '%-5s' % (i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
        print('-----------------------------------------------------------------------------------')

    def older(arg1, arg2):
        if int(arg1[2]) < int(arg2[2]):
            return True
        elif int(arg1[2]) == int(arg2[2]) and int(arg1[1]) < int(arg2[1]):
            return True
        elif int(arg1[2]) == int(arg2[2]) and int(arg1[1]) == int(arg2[1]) and int(arg1[0]) < int(arg2[0]):
            return True
        else:
            return False

    def sort_list(list):
        #iOlderUser = list[j]
        #print(iOlderUser)
        for i in list:
            iOlderUser = list[0]
            date = i.birthday.split('.')
            dateOlder = iOlderUser.birthday.split('.')
            #print(date)
            #print(dateOlder)
            #print(i)
            if Kontroler.older(date, dateOlder):
                i, iOlderUser = iOlderUser, i

            #else:
               # list.sort(key=lambda i: i.name)
                #print(list.i)
                #print(list.iOlderUser)
                #list.sort(key=lambda i: i.name)

        return list





    def printList(list):  # function for printing lists
        for i in list:
            print('%-12s %-12s %-14s %-12s %-10s %-5s'
                  % (i.name, i.surname, i.birthday, i.stipend, i.facultet, i.kusrs))




list_all_chuvaki = Kontroler('C:\\Users\\svetlana.pilgun\\PycharmProjects\\Projects_test\\File_kurs.txt').readFile()
""" пытяюсь посомтрть что считывается """

#print (list_all_chuvaki)

#Kontroler.DisplayData(list_all_chuvaki)
""" пытяюсь посомтрть что выводится """

student_list, prepod_List = Kontroler.person_list(list_all_chuvaki)
print ('Студенты: ')
Kontroler.printList(student_list)
Kontroler.sort_list(student_list)

Kontroler.printList(student_list)