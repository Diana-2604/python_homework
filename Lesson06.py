# TASK 1

# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.​
# Пример:​[1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]​

# from collections import Counter

# my_list = [1, 2, 3, 5, 1, 5, 3, 10]

# total = dict(Counter(my_list))

# res = dict(filter(lambda x: x[1] < 2, total.items()))

# unique = list(res.keys())

# print('Исходная последовательность: ', my_list)    
# print('Уникальные элементы последовательности: ', unique)


# TASK 2

# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# from functools import reduce

# my_list = [1, 4, 2, 6, 4, 1, 7]

# res = reduce(lambda l, x: l+[x] if x not in l else l, my_list, [])

# print('Исходная последовательность: ', my_list)    
# print('Неповторяющиеся элементы последовательности: ', res)


# TASK3

# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# data = list(map(int,input('Введите несколько чисел через пробел: ').split()))
# print(list(enumerate(data)))

# res = [data[i] for i in range(0, len(data)) if i % 2 == 1]

# print(sum(res))


# TASK 4 

# Преобразовать набор списков:
# users = ['user1','user2','user3','user4','user5']
# ids = [4, 5, 8, 3, 6]
# salary = [111,222,333]
# в другой набор:
# ['user1', 4, 111]
# ['user2', 5, 222]
# ['user3', 8, 333]
# и потом вернуть в исходное состояние:
# ['user1', 'user2', 'user3']
# [4, 5, 8]
# [111, 222, 333]

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 8, 3, 6]
# salary = [111,222,333]

# print('Первый набор: ')
# a, b, c = map(list, zip(users, ids, salary))
# print(a, b, c, sep="\n")

# print('Второй набор: ')
# a, b, c = map(list, zip(a, b, c))
# print(a, b, c, sep="\n")

# TASK 5

# В файле хранятся числа. Нужно выбрать четные и составить список пар (число; квадрат числа).
# Пример: [1, 2, 3, 5, 8, 15, 23, 38] --> [(2, 4), (8, 64), (38, 1444)]

data = '1 2 3 5 8 15 23 38'.split()
data = list(map(int, data))
data = list(filter(lambda e: not e % 2, data))
data = list(map(lambda e: (e, e**2), data))

print(data)


