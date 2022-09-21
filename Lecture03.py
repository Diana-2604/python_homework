# Урок 3. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension

# Lambda - сокращенное написание анонимных функций

# sum = lambda x,y : x + y

# def calc(op, a,b):
#     print(op(a, b))

# calc(sum, 4, 5) # --> 9

#TASK
# Объявите анонимную (лямбда) функцию для определения вхождения в переданную ей строку фрагмента "plr". 
# То есть, функция должна возвращать True, если такой фрагмент присутствует в строке, и False в противном случае.

# contains = lambda s, sample = 'plr': sample in s
# s = input()
# print(contains(s))

# List comprehension - упрощенное создание списков и обработка данных

# [exp for item in iterable] # exp = expression - выражение
# [exp for item in iterable (if conditional)]

# TASK
# В файле хранятся числа. Нужно выбрать четные и составить список пар (число; квадрат числа).
# Пример: [1, 2, 3, 5, 8, 15, 23, 38] --> [(2, 4), (8, 64), (38, 1444)]

# def f(x):
# 	return x**2

# list = [1, 2, 3, 5, 8, 15, 23, 38]

# res = [(list[i], f(list[i])) for i in range(0, len(list)) if list[i] % 2 == 0]

# print(res)

# OR: 1 2 3 5 8 15 23 38 --> [(2, 4), (8, 64), (38, 1444)]

# data = '1 2 3 5 8 15 23 38'.split()
# data = list(map(int, data))
# data = list(filter(lambda e: not e % 2, data))
# data = list(map(lambda e: (e, e**2), data))
# print(data)

# print(data)

# Функция map - применяет указанную функцию к каждому элементу итерируемого объекта и возвращает итератор с новыми объектами

# li = [x for x in range(1,20)]
# print(li)

# li = list(map(lambda x: x+10, li)) # каждый элемент списка увеличивается на 10
# print(li)

# Функция filter - применяет указанную функцию к каждому элементу итерируемого объекта и возвращает итератор с теми объектами,
# для которых функция вернула True

# Пример: f(x) ⇒ x - чётное
# filter(f, [1, 2, 3, 4, 5]) --> [2, 4]

# data = [x for x in range(10)]
# print(data)

# res = list(filter(lambda x: x%2 == 0, data)) # same as 'lambda x: not x%2'
# print(res)

# Функция zip - применяется к набору итерируемых объектов и возвращает итератор с кортежами из элементов входных данных

# zip ([1, 2, 3], [ ‘о‘, ‘д‘, ‘т‘], [‘f’,’s’,’t’]) --> [(1, 'о', 'f'), (2, 'д', 's'), (3, 'т', 't')]

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 8, 3, 6]

# data = list(zip(users, ids))
# print(data) # --> ('user1', 4), ('user2', 5), ('user3', 8), ('user4', 3), ('user5', 6)]

# Возвращает минимальное число возможных кортежей:

# salary = [111, 222, 333]
# list = list(zip(users, ids, salary))
# print(list) # --> [('user1', 4, 111), ('user2', 5, 222), ('user3', 8, 333)]

# Функция enumerate применяется к итерируемому объекту и возвращает новый итератор с кортежами из индекса и элементов входных данных

# enumerate(['Казань', 'Смоленск', 'Рыбки', 'Чикаго']) --> [(0, 'Казань'), (1, 'Смоленск'), (2, 'Рыбки'), (3, 'Чикаго')]

# users = ['user1', 'user2', 'user3', 'user4', 'user5']

# data = list(enumerate(users))
# print(data) # --> [(0, 'user1'), (1, 'user2'), (2, 'user3'), (3, 'user4'), (4, 'user5')]