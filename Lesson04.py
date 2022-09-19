# TASK1

# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# import math
# d = float(input('Введите необходимую точность вычисления: '))

# r = 0
# while d < 1:
#     d = d * 10
#     r += 1

# pi = math.pi
# c = 5
# x = 12.5

# print('{pi} = ', f'{pi:.{r}f}')
# print('{c} = ', f'{c:.{r}f}')
# print('{x} = ', f'{x:.{r}f}')

# TASK 2

# Задайте натуральное число N (N > 0). Напишите программу, которая составит список простых множителей числа N.

# n = int(input('Please enter your number: '))

# def Factor(n):
#     Ans = []
#     d = 2
#     while d * d <= n:
#         if n % d == 0:
#             Ans.append(d)
#             n //= d 
#         else:
#             d += 1
#     if n > 1:
#         Ans.append(n)
#     return Ans

# print(Factor(n))


# TASK 3

# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# list = [1, 4, 2, 6, 4, 1, 7]
# res = []
# i = 0
# for i in range(0, len(list)):
#     if list[i] not in res:
#         res.append(list[i])
#     i += 1

# print('Исходная последовательность: ', list)    
# print('Неповторяющиеся элементы последовательности: ', res)


# TASK 4

# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# import random

# # k = int(input('Значение натуральной степени k: '))
# k = 2
# a = random.randint(0, 100)
# b = random.randint(0, 100)
# c = random.randint(0, 100)

# f = open('text.txt','a')

# # Для генерации новых рандомных коэффициентов, дозапись в файл производится поочередно:
# # f.write(str(a) + "*x^" + str(k) + " + " + str(b) + "*x" + " + " + str(c) + " = 0" + "\n")
# # f.write(str(a) + "*x^" + str(k) + " + " + str(c) + " = 0" + "\n")
# f.write(str(a) + "*x^" + str(k) + " = 0" + "\n")
# f.close()


# TASK 5

# Даны два файла, в каждом из которых находится
# запись многочлена. Задача - сформировать файл,
# содержащий сумму многочленов.

f1 = open('mn1.txt', 'r')
f2 = open('mn2.txt', 'r')
sum = open('sum.txt', 'w')

mn1 = f1.read().split(" ")
mn2 = f2.read().split(" ")
for i in range(0, len(mn1)):
    if mn1[i] != mn2[i]:
        mn1[i] = int(mn1[i]) + int(mn2[i])
mn = ''
for i in mn1:
    mn += str(i) + ' '
print(mn)
sum.write(mn)

f1.close()
f2.close()
sum.close()

