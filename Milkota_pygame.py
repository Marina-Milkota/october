# import pygame

# pygame.init
# dis = pygame.display.set_mode((500,500))
# size = pygame.display.get_window_size()
# pygame.display.set_caption('Snake_game')
#
# white = (255,255,255)
# blue = (0,0,255)
# red = (255,0,0)
#
# game_over = False
#
# #Координаты головы змейки (фактические)
# x1 = 300
# y1 = 400
#
# #На сколько изменить x1 или y1:
# x1_change = 0
# y1_change = 0
#
# #Завели переменную для тактовой частоты (какая должна быть задержка между движениями)
# clock = pygame.time.Clock()
#
# # font_style = pygame.font.SysFont(None, 50)
# #
# # def message(msg,color):
# #     mesg = font_style.render(msg, True, color)
# #     dis.blit(mesg, [size[0], size[1]])
#
# while not game_over:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             game_over = True
#         if event.type == pygame.KEYDOWN: #проверяем, нажал ли пользователь клавишу
#             if event.key == pygame.K_LEFT:
#                 x1_change = -10
#                 y1_change = 0
#             if event.key == pygame.K_RIGHT:
#                 x1_change = 10
#                 y1_change = 0
#             if event.key == pygame.K_UP:
#                 x1_change = 0
#                 y1_change = -10
#             if event.key == pygame.K_DOWN:
#                 x1_change = 0
#                 y1_change = 10
#     x1 += x1_change
#     y1 += y1_change
#     dis.fill(white)
#     pygame.draw.rect(dis, blue, (x1, y1, 10, 10))  # первые 2 аргумента - это положение на экране,3-4 аргументы - размер
#     pygame.display.update()  # после изменений экран нужно обновить
#
#     if y1>=size[1] or y1<=0:
#         game_over = True
#     if x1 >= size[0]:
#         x1 = 0
#     elif x1 <= 0:
#         x1 = size[0]
#
#     x1 += x1_change
#     y1 += y1_change
#     # dis.fill(white)
#
#     clock.tick(10) #сколько фреймов происходит в секунду (кадров в секунду fps)
#
# # message("You lost",red)
# # pygame.display.update()
# # time.sleep(2)
#
# pygame = quit()
# quit()

#ДЗ на вторник: сделать еду для змейки (змейка должна увеличиваться), по желанию: счетчик очков и поменять фон игры

import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 600
dis_height = 500

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake_game_Milkota')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
