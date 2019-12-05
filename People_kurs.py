class Univer_People:
    def __init__(self, vtype, name, surname, birthday, facultet):
        self.vtype = vtype
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.facultet = facultet
        #self.money = money
        #self.years = years

class Student (Univer_People):
    def __init__(self, stipend, kurs):
        self.stipend = stipend
        self.kurs = kurs

class Prepod (Univer_People):
    def __init__(self, zp, stazh):
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


    def DisplayData(list):
        """ Метод вывода информации """
        for (i) in list:
            print(i[1:])

list_all_chuvaki = Kontroler('C:\\Users\\svetlana.pilgun\\PycharmProjects\\Projects_test\\File_kurs.txt').readFile()
    """ пытяюсь посомтрть что считывается """

Kontroler.DisplayData(list_all_chuvaki)
""" пытяюсь посомтрть что выводится """

