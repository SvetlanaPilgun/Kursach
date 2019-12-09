import People_kurs


list_all_chuvaki = People_kurs.Kontroler('C:\\Users\\svetlana.pilgun\\PycharmProjects\\Projects_test\\File_kurs.txt').readFile()
""" считываем данные из файла"""

People_kurs.Kontroler.DisplayData(list_all_chuvaki)
""" выводим содержимое файла """
student_list, prepod_List = People_kurs.Kontroler.person_list(list_all_chuvaki)
""" создаем два отдельных списка студентов и преподавателей """
print('Студенты: ')
print()
People_kurs.Kontroler.printList1(student_list)
""" выводим студентов """
People_kurs.Kontroler.sort_list(student_list)
""" сортируем студентов """
print('------------------------------------------------------------------')
print('Отсортированные студенты по имени: ')
print()
People_kurs.Kontroler.printList1(student_list)
""" выводим уже отсортированных студентов """
print('------------------------------------------------------------------')
print('Преподаватели: ')
print()
People_kurs.Kontroler.printList2(prepod_List)
""" выводим преподавателей """
People_kurs.Kontroler.sort_list(prepod_List)
""" сортируем преподавателей """
print('------------------------------------------------------------------')
print('Отсортированные преподаватели по имени: ')
print()
People_kurs.Kontroler.printList2(prepod_List)
""" выводим уже отсортированных преподавателей """





