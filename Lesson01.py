# TASK 1
# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

# n = int(input('Please enter your number: '))
# weekday = range(1,6)
# weekend = range(6,8)
# if n in weekday:
#     print("sorry, it isn't weekend yet")
# elif n in weekend:
#     print("hurray, it's weekend!")
# else:
#     print("unknown day of the week")

# TASK2
# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# x = int(input('X = '))
# y = int(input('Y = '))
# z = int(input('Z = '))

# if not(x or y or z) == (not x and not y and not z):
#     print('true')
# else:
#     print('false')

# TASK 2 SOLUTION MODIFIED

for x in range(2):
    for y in range(2):
        for z in range(2):
            print(not (x or y or z) == (not x and not y and not z))
            print(x,y,z)


# TASK3
# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# x = int(input('X: '))
# y = int(input('Y: '))

# pos = range(1,100)
# neg = range(-100,0)

# if x in pos and y in pos:
#     print('quarter 1')
# elif x in neg and y in pos:
#     print('quarter 2')
# elif x in neg and y in neg:
#     print('quarter 3')
# elif x in pos and y in neg:
#     print('quarter 4')
# elif (x == 0 and y == 0):
#     print('zero point')
# elif x == 0:
#     print('the point is on the X-axis')
# elif y == 0:
#     print('the point is on the Y-axis')
# else:
#     print('please fix the range to check values > 99')

# TASK4
# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# qr = int(input('Please enter the quarter number: '))

# qr1 = '{X > 0, Y > 0}'
# qr2 = '{X < 0, Y > 0}'
# qr3 = '{X < 0, Y < 0}'
# qr4 = '{X > 0, Y < 0}'

# if qr == 1:
#     print(qr1)
# elif qr == 2:
#     print(qr2)
# elif qr == 3:
#     print(qr3)
# elif qr == 4:
#     print(qr4)
# else:
#     print("Please enter a valid quarter number (1-4)")

# TASK5
# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# Ax = int(input('Ax: '))
# Ay = int(input('Ay: '))

# Bx = int(input('Bx: '))
# By = int(input('By: '))

# AB = ((Bx - Ax)**2 + (By - Ay)**2)**(0.5)
# print(round(AB,3))
