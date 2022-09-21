# TASK1

# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# with open("words.txt", "r") as fin:
#     for line in fin:
#         words = line.split()
#         for word in words:
#             if "абв" in word:
#                 words.remove(word)
#                 sentence = " ".join(words)
#                 print(sentence)


# TASK 2

# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

# import random

# candy = 2021
# grab = 28
# gamer1 = random.randint(1,3)

# if gamer1 == 1:
#     gamer2 = 2
# elif gamer1 == 2:
#     gamer2 = 1

# steps = candy // grab
# step1 = candy % grab

# print('Минимальное число ходов: ', steps + 1)
# print('Число конфет в первый ход: ', step1)


# TASK 3
# Создайте программу для игры в ""Крестики-нолики""

# import pygame
# import sys

# def check_win(mas,sign):
#     zeroes = 0
#     for row in mas:
#         zeroes += row.count(0)
#         if row.count(sign) == 3:
#             return f'{sign} wins!'
#     for col in range(3):
#         if mas[0][col] == sign and mas[1][col] == sign and mas[2][col] == sign:
#             return f'{sign} wins!'
#         if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:
#             return f'{sign} wins!'
#         if mas[0][2] == sign and mas[1][1] == sign and mas[2][0] == sign:
#             return f'{sign} wins!'
#         if zeroes == 0:
#             return 'Peace :)'
#         return False

# pygame.init()
# size_block = 100
# margin = 15
# width = height = size_block*3 + margin*4

# size_window = (width, height)
# screen = pygame.display.set_mode(size_window)
# pygame.display.set_caption("Крестики-нолики")

# black = (60, 60, 60)
# red = (255, 99, 71)
# green = (60, 179, 113)
# white = (240, 240, 240)
# yellow = (255, 165, 0)
# mas = [[0]*3 for i in range(3)] # массив из 9 пустых клеток
# query = 0 # очередность хода
# game_over = False

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
#             x_mouse, y_mouse = pygame.mouse.get_pos()
#             col = x_mouse // (size_block + margin)
#             row = y_mouse // (size_block + margin)
#             if mas[row][col] == 0:
#                 if query % 2 == 0:
#                     mas[row][col] = 'x'
#                 else:
#                     mas[row][col] = 'o'
#                 query+= 1
#         elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: # перезапуск игры при нажатии пробела
#             game_over = False
#             mas = [[0]*3 for i in range(3)] 
#             query = 0
#             screen.fill(black)
#     if not game_over:
#         for row in range(3):
#             for col in range(3):
#                 if mas[row][col] == 'x':
#                     color = red
#                 elif mas[row][col] == 'o':
#                     color = green
#                 else:
#                     color = white
#                 x = col*size_block + (col+1)*margin
#                 y = row*size_block + (row+1)*margin
#                 pygame.draw.rect(screen, color, (x,y,size_block,size_block))
#                 if color == red:
#                     pygame.draw.line(screen,white,(x+5,y+5), (x+size_block-5, y+size_block-5),6)
#                     pygame.draw.line(screen,white,(x+size_block-5,y+5), (x+5, y+size_block-5),6)
#                 elif color == green:
#                     pygame.draw.circle(screen,white,(x+size_block//2, y+size_block//2), size_block//2 - 3, 4)
#     if (query-1)%2 == 0:
#         game_over = check_win(mas,'x')
#     else:
#         game_over = check_win(mas,'o')

#     if game_over:
#         screen.fill(black)
#         font = pygame.font.SysFont('peachyday', 80)
#         text1 = font.render(game_over, True, yellow)
#         text_rect = text1.get_rect()
#         text_x = screen.get_width() / 2 - text_rect.width / 2
#         text_y = screen.get_height() / 2 - text_rect.height / 2
#         screen.blit(text1, [text_x, text_y])
    
#     pygame.display.update()

# TASK 4

# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные и выходные данные хранятся в отдельных текстовых файлах.

f1 = open('original.txt', 'r')
f2 = open('encode.txt', 'w')
f3 = open('decode.txt', 'w')

def encode_message(message):
    encoded_string = ""
    i = 0
    while (i <= len(message)-1):
        count = 1
        ch = message[i]
        j = i
        while (j < len(message)-1): 
        #if the character at the current index is the same as the character at the next index.
        #If the characters are the same, the count is incremented to 1   
            if (message[j] == message[j + 1]): 
                count = count + 1
                j = j + 1
            else: 
                break
        # the count and the character is concatenated to the encoded string
        encoded_string = encoded_string + str(count) + ch
        i = j + 1
    return encoded_string

def decode_message(our_message):
    decoded_message = ""
    i = 0
    j = 0
    # splitting the encoded message into respective counts
    while (i <= len(our_message) - 1):
        run_count = int(our_message[i])
        run_word = our_message[i + 1]
        # displaying the character multiple times specified by the count
        for j in range(run_count):
            # concatenated with the decoded message
            decoded_message = decoded_message+run_word
            j = j + 1
        i = i + 2
    return decoded_message

# the original string
our_message = f1.read()
# pass in the original string
encoded_message = encode_message(our_message)
f2.write(encoded_message)
# pass in the decoded string
decoded_message = decode_message(encoded_message)
f3.write(decoded_message)

print("Original string: [" + our_message + "]")
print("Encoded string: [" + encoded_message +"]")
print("Decoded string: [" + decoded_message +"]")

f1.close()
f2.close()
f3.close()

