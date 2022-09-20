# TASK1

# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# list = list(map(int,input('Введите несколько чисел через пробел: ').split()))
# print(list)

# i = 1
# sum = 0

# while i < len(list):
#     sum += list[i]
#     i += 2

# print(sum)

# OR

# my_list = [2, 3, 5, 9, 3]
# print(sum(my_list[1::2])) # сумма элементов списка, начиная с 1-го, с шагом 2

# TASK 2 

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# import math

# list = list(map(int,input('Введите несколько чисел через пробел: ').split()))
# print(list)

# line = math.ceil(len(list)/2)

# mult = 0
# multilist = []

# for i in range(0, line):
#     mult = list[i]*list[-1-i]
#     multilist.append(mult)

# print(multilist)


# TASK3

# Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# import math
# fractlist = []

# list = [1.1, 1.2, 3.1, 5, 10.01]  
# for i in list:
#     x = math.modf(i) # returns the fractional and integer parts of the number in a two-item tuple
#     if x[0] != 0:
#         fractlist.append(round(x[0],2))

# print(list)

# dif = max(fractlist) - min(fractlist)
# print(dif)


# TASK 4

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# num = int(input('Please enter your number: '))
# print(f'{num:b}')


# TASK5

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов (Негафибоначчи).

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# num = int(input('Введите число членов последовательности Фибоначчи: '))

# negafib = [1,-1]
# while len(negafib) < num:
#     negafib.append(negafib[-2] - negafib[-1])
# negafib.reverse()

# fib = [0,1]
# while len(fib) <= num:
#     fib.append(fib[-1] + fib[-2])
# print(negafib + fib)



