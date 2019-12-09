
class Student:
    """ Класс студентов """
    def __init__(self, name, surname, birthday, stipend, facultet, kusrs):
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.facultet = facultet
        self.stipend = stipend
        self.kusrs = kusrs


class Prepod:
    """ Класс преподавателей """
    def __init__(self, name, surname, birthday, zp, facultet, stazh):
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.facultet = facultet
        self.zp = zp
        self.stazh = stazh


class Kontroler:
    """ Класс контролер """
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
                line = Student(i[name], i[surname], i[birthday], i[money], i[facultet], i[count_year])
                students.append(line)
            elif i[0] == 'преподаватель':
                line = Prepod(i[name], i[surname], i[birthday], i[money], i[facultet], i[count_year])
                prepods.append(line)
        return students, prepods

    def DisplayData(list):
        """ Метод вывода информации """
        type_p = 0
        name = 1
        surname = 2
        birthday = 3
        money = 4
        facultet = 5
        count_year = 6
        print('Список всех чуваков:')
        print()
        print('%-14s' ': ' '%-10s' '%-12s' '%-17s' '%-14s' '%-11s' '%-5s' % ('Должность', 'Имя', 'Фамилия', 'Дата_Рождения', 'стипендия/зп', 'Факульткет', 'Курс/Стаж'))
        print()
        for i in list:
            print('%-14s' ': ' '%-10s' '%-12s' '%-17s' '%-14s' '%-11s' '%-5s' % (i[type_p], i[name], i[surname], i[birthday], i[money], i[facultet], i[count_year]))
        print('---------------------------------------------------------------------------------------')

    def printList1(list):
        """ Метод вывода студентов """
        for i in list:
            print('%-12s %-12s %-14s %-12s %-10s %-5s'
                  % (i.name, i.surname, i.birthday, i.stipend, i.facultet, i.kusrs))

    def printList2(list):
        """ Метод вывода преподавателей """
        for i in list:
            print('%-12s %-12s %-14s %-12s %-10s %-5s'
                  % (i.name, i.surname, i.birthday, i.zp, i.facultet, i.stazh))


    def sort_list(list):
        """ Метод сортировки списка по имени """
        list.sort(key=lambda i: i.name)
        return list



