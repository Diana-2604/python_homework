# TASK1

# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

# num = input("Введите дробное число в формате 'XX.XX': ")
# x = num.split(".") 
# a = int(x[0]) # целая часть
# b = int(x[1]) # дробная часть
# print("a =", a)
# print("b =", b)
# sum = 0

# while (a != 0): # перемножаем числа целой части
#     sum = sum + a % 10
#     a = a // 10
# while (b != 0): # перемножаем числа дробной части
#     sum = sum + b % 10
#     b = b // 10

# print("Сумма цифр равна:", sum)

# TASK 2

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# N = int(input('Введите число N: '))
# i = 1
# n = 1
# list = []

# while i <= N:
#     n = n*i
#     list.append(n)
#     i+=1

# print(list)


# TASK 3

# Задайте список из n чисел последовательности $(1+(1/n))^n$ и выведите на экран их сумму.

# n = int(input('Введите число: '))
# sum = 0

# for i in range(1, n+1):
#     sum = sum + ((1+1/i)**i)

# print(round(sum,2))

# TASK 5

# Реализуйте алгоритм перемешивания списка.

# import random

# list = ['a', 'b', 'c', 'd', 'e']

# random.shuffle(list)

# print(list)
