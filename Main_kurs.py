import People_kurs


list_all_chuvaki = People_kurs.Kontroler('C:\\Users\\svetlana.pilgun\\PycharmProjects\\Projects_test\\File_kurs.txt').readFile()
""" пытяюсь посомтрть что считывается """

People_kurs.Kontroler.DisplayData(list_all_chuvaki)
""" пытяюсь посомтрть что выводится """
student_list, prepod_List = People_kurs.Kontroler.person_list(list_all_chuvaki)
print ('Студенты: ')
People_kurs.Kontroler.printList(student_list)
People_kurs.Kontroler.sort_list(student_list)

