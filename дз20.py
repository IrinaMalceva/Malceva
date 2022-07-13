# 1.Сформулируйте SQL запрос для создания таблицы movies.
# Поля: movie_id, FIO TEXT, ch INTEGER, mm INTEGER, yy INTEGER
# 2. Создать функции (Функции вызывать в цикле, чтоб у пользователя был выбор):
# 1. Принять сотрудника  (заполнение делать с клавиатуры)
# 2. Получения данных обо всех сотрудниках
# 3. Получения данных об одном сотруднике по id
# 4. Посмотреть календарь месяца
# 0. Выход


import calendar
i = 0

def in_ch():
    ch = int(input("число  "))
    if ch > 31:
        print("Неверный ввод")
        ch = int(input(" повторите число  "))
    return ch

def in_month():
    mm = int(input('месяц  '))
    if mm > 12:
        print("Неверный ввод")
        mm = int(input('повторите месяц  '))
    return mm

def in_year():
    yy = int(input("год  "))
    if yy > 2022:
        print("Неверный ввод")
        yy = int(input("повторите год  "))
    return yy

def of_month(mm, yy):
    import calendar
    print(calendar.month(themonth=mm, theyear=yy))

import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS movies (movie_id INTEGER PRIMARY KEY AUTOINCREMENT, FIO TEXT, ch INTEGER, mm INTEGER, yy INTEGER ) ''')
conn.commit()

wer = 0
while wer >= 0:
    print('1. Принять сотрудника  ' '\n' '2. Получения данных обо всех сотрудниках' '\n' 
          '3. Получения данных об одном сотруднике по id''\n' '4. Посмотреть календарь месяца''\n' '0. Выход')
    a = int(input('Введите ваш выбор? '))
    if a == 1:
        print('Введите анкетные данные:')
        FIO = input("Введите фамилию, имя, отчество полностью  ")
        print("Дата рождения:__/__/____")

        ch = in_ch()
        mm = in_month()
        yy = in_year()
        print(FIO, ch, mm, yy)

        cursor.execute('''INSERT INTO movies(FIO, ch, mm, yy) VALUES(?,?,?,?)''', (FIO, ch, mm, yy))
        conn.commit()
        print('----------------------------------------------------------------')

        # 1, Петров Иван Иванович, 2, 3, 1970

    elif a == 2:
        cursor.execute('''SELECT * FROM movies''')
        k = cursor.fetchall()
        for i in k:
            s = ','.join([str(s) for s in i])
            print(s)
        print('----------------------------------------------------------------')

    elif a == 3:
        q = int(input('Введите номер сотрудника: '))
        cursor.execute('''SELECT  * FROM movies ''')
        w = cursor.fetchall()


        print(len(w))
        if q > len(w):
            print("Неверный ввод,  количество сотрудников в базе :",  len(w))
            q = int(input('Повторите номер сотрудника: '))


        print(w[q - 1])
        print('----------------------------------------------------------------')
    elif a == 4:
        # ch = in_ch()
        mm = in_month()
        yy = in_year()
        of_month(mm, yy)

    elif a == 0:
        break





