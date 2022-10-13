# #ДЗ на вторник:
# 1. Создайте новую Базу данных
# Поля: id, 2 целочисленных поля
# Целочисленные поля заполняются рандомно от 0 до 9
# Выберите случайную запись из БД
# Если каждое число данной записи чётное,
# то удалите эту запись, если нечётное, то обновите данные в ней на(2,2)
#
# import sqlite3, random
# conn = sqlite3.connect('my_data_base.db')
# cursor = conn.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS task_1
# (id INTEGER PRIMARY KEY AUTOINCREMENT, k_1 INTEGER, k_2 INTEGER)''')
# a = random.randint(0,10)
# b = random.randint(0,10)
# cursor.execute('''INSERT INTO task_1 (k_1, k_2) VALUES (?,?)''',(a,b))
# conn.commit()
# cursor.execute('''SELECT id FROM task_1''')
# n = cursor.fetchall()
# r = random.choice(n)
# print(r)
# cursor.execute('''SELECT k_1,k_2 FROM task_1 WHERE id=?''',r)
# for i in cursor:
#     print(i)
#     if i[0]%2 ==0 and i[1]%2==0:
#         cursor.execute('''DELETE FROM task_1 WHERE id=?''',r)
#
#     elif i[0]%2 !=0 and i[1]%2 !=0:
#         cursor.execute('''UPDATE task_1 SET k_1=2, k_2=2 WHERE id=?''',r)
#
# conn.commit()
# cursor.execute('''SELECT * FROM task_1''')
# print(*cursor)
#


# 2. Создать 2 таблицы в Базе Данных
# Одна будет хранить текстовые данные(1 колонка)
# Другая числовые(1 колонка)
# Есть список, состоящий из чисел и слов.
#  my_list = [‘Home’, ‘Work’, 29, 9, 2022]
# Если элемент списка слово, записать его в соответствующую таблицу,
# затем посчитать длину слова и записать её в числовую таблицу
# Если элемент списка число: проверить, если число чётное записать его в таблицу чисел,
# если нечётное, то записать во вторую таблицу слово: «нечётное»
# Если число записей во второй таблице больше 5, то удалить 1 запись в первой таблице.
# Если меньше, то обновить 1 запись в первой таблице на «hello»
#
# import random
# import sqlite3
# my_list = ['Home', 'Work', 29, 9, 2022]
# conn = sqlite3.connect('t_2.db')
# cursor = conn.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS t_2_1
# (id INTEGER PRIMARY KEY AUTOINCREMENT, text TEXT)''')
# cursor.execute('''CREATE TABLE IF NOT EXISTS t_2_2
# (id INTEGER PRIMARY KEY AUTOINCREMENT, numbers INTEGER)''')
# for i in my_list:
#     if type(i) == str:
#         cursor.execute('''INSERT INTO t_2_1(text) VALUES (?)''', (i,))
#         conn.commit()
#         cursor.execute('''INSERT INTO t_2_2(numbers) VALUES (?)''', (len(i),))
#         conn.commit()
#     elif type(i) == int:
#         if i%2!=0:
#             cursor.execute('''INSERT INTO t_2_2(numbers) VALUES (?)''',(i,))
#             conn.commit()
#         else:
#             cursor.execute('''INSERT INTO t_2_1(text) VALUES ('Нечетное') ''')
#             conn.commit()
# cursor.execute('''SELECT * FROM t_2_1''')
# spis1 = cursor.fetchall()
# print(spis1)
# cursor.execute('''SELECT * FROM t_2_2''')
# spis2 = cursor.fetchall()
# print(spis2)
#
# if len(spis2)>5:
#     cursor.execute('''DELETE FROM t_2_1 WHERE id=?''',(spis1[0][0],))
#     conn.commit()
# elif len(spis2)<5:
#     cursor.execute('''UPDATE t_2_1 SET text='Hello' WHERE id=?''',(spis1[0][0],))
#     conn.commit()
#
# cursor.execute('''SELECT * FROM t_2_1''')
# print(*cursor)
# cursor.execute('''SELECT * FROM t_2_2''')
# print(*cursor)
#


# 3. Заполнить таблицу БД названиями песен с указанием их длительности
# (то есть колонка с названием и колонка со временем в секундах)
# Из этой таблицы собрать все записи, с длительностью больше 60 секунд и записать их в текстовый файл (название и время).

import sqlite3
conn = sqlite3.connect('Task_3.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS music
(id INTEGER PRIMARY KEY AUTOINCREMENT,songs TEXT, time INTEGER)''')
while True:
    a = input('Введите песню: ')
    b = int(input('Введите длительность в секундах: '))
    cursor.execute('''INSERT INTO music(songs, time) VALUES (?,?)''',(a,b))
    conn.commit()
    c = input('Еще?-введите 1, для завершения-2  ')
    if c=='2':break

cursor.execute('''SELECT * FROM music''')
with open('text.txt','w') as f:
    for i in cursor:
        print(i)
        if i[2]>60: f.write(str(i) + '\n')
