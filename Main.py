import pygame
from pygame import *


def load():
    pygame.init()

    size = width, height = 1000, 1000
    speed = [2, 2]
    black = 0, 0, 0

    screen = pygame.display.set_mode(size)

    ball = pygame.image.load("icon.png")
    ballrect = ball.get_rect()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]
        screen.fill(255)
        screen.blit(ball, ballrect)
        pygame.display.flip()

def map(h,surface, color):
    surface.fill(background)
    pygame.draw.line(surface, color, (h*0.100, h*0.366), (h*0.900, h*0.366), 5)
    pygame.draw.line(surface, color, (h*0.100, h*0.633), (h*0.900, h*0.633), 5)
    pygame.draw.line(surface, color, (h*0.366, h*0.100), (h*0.366, h*0.900), 5)
    pygame.draw.line(surface, color, (h*0.633, h*0.100), (h*0.633, h*0.900), 5)
    pygame.display.flip()

def check(h, poz):
    if poz[0] >= h*0.100 and poz[0] < h*0.366 and poz[1] >= h*0.100 and poz[1] < h*0.366:
        return 0
    elif poz[0] >= h*0.100 and poz[0] < h*0.366 and poz[1] >= h*0.366 and poz[1] < h*0.633:
        return 1
    elif poz[0] >= h*0.100 and poz[0] < h*0.366 and poz[1] >= h*0.633 and poz[1] < h*0.900:
        return 2



    elif poz[0] >= h*0.366 and poz[0] < h*0.633 and poz[1] >= h*0.100 and poz[1] < h*0.366:
        return 3
    elif poz[0] >= h*0.366 and poz[0] < h*0.633 and poz[1] >= h*0.366 and poz[1] < h*0.633:
        return 4
    elif poz[0] >= h*0.366 and poz[0] < h*0.633 and poz[1] >= h*0.633 and poz[1] < h*0.900:
        return 5


    elif poz[0] >= h*0.633 and poz[0] < h*0.900 and poz[1] >= h*0.100 and poz[1] < h*0.366:
        return 6
    elif poz[0] >= h*0.633 and poz[0] < h*0.900 and poz[1] >= h*0.366 and poz[1] < h*0.633:
        return 7
    elif poz[0] >= h*0.633 and poz[0] < h*0.900 and poz[1] >= h*0.633 and poz[1] < h*0.900:
        return 8

def draw_object(h, surface, color, turn):
    if num_field == 0:
        if turn == 1:
            pygame.draw.circle(surface, color, (h*0.233, h*0.233), h*0.100, 3)
        elif turn == -1:
            pygame.draw.line(surface, color, (h*0.165, h*0.165), (h*0.300, h*0.300), 3)
            pygame.draw.line(surface, color, (h*0.300, h*0.165), (h*0.165, h*0.300), 3)
        return 0
    elif num_field == 1:
        if turn == 1:
            pygame.draw.circle(surface, color, (h*0.233, h*0.499), h*0.100, 3)
        elif turn == -1:
            pygame.draw.line(surface, color, (h*0.165, h*0.431), (h*0.300, h*0.568), 3)
            pygame.draw.line(surface, color, (h*0.300, h*0.431), (h*0.165, h*0.568), 3)
    elif num_field == 2:
        if turn == 1:
            pygame.draw.circle(surface, color, (h*0.233, h*0.766), h*0.100, 3)
        elif turn == -1:
            pygame.draw.line(surface, color, (h*0.165, h*0.698), (h*0.300, h*0.835), 3)
            pygame.draw.line(surface, color, (h*0.300, h*0.698), (h*0.165, h*0.835), 3)



    elif num_field == 3:
        if turn == 1:
            pygame.draw.circle(surface, color, (h*0.499, h*0.233), h*0.100, 3)
        elif turn == -1:
            pygame.draw.line(surface, color, (h*0.430, h*0.165), (h*0.568, h*0.300), 3)
            pygame.draw.line(surface, color, (h*0.568, h*0.165), (h*0.430, h*0.300), 3)
    elif num_field == 4:
        if turn == 1:
            pygame.draw.circle(surface, color, (h*0.499, h*0.499), h*0.100, 3)
        elif turn == -1:
            pygame.draw.line(surface, color, (h*0.430, h*0.430), (h*0.568, h*0.568), 3)
            pygame.draw.line(surface, color, (h*0.568, h*0.434), (h*0.434, h*0.568), 3)
    elif  num_field == 5:
        if turn == 1:
            pygame.draw.circle(surface, color, (h*0.499, h*0.766), h*0.100, 3)
        elif turn == -1:
            pygame.draw.line(surface, color, (h*0.430, h*0.698), (h*0.568, h*0.835), 3)
            pygame.draw.line(surface, color, (h*0.568, h*0.698), (h*0.430, h*0.835), 3)


    elif num_field == 6:
        if turn == 1:
            pygame.draw.circle(surface, color, (h*0.766, h*0.233), h*0.100, 3)
        elif turn == -1:
            pygame.draw.line(surface, color, (h*0.698, h*0.165), (h*0.835, h*0.300), 3)
            pygame.draw.line(surface, color, (h*0.835, h*0.165), (h*0.698, h*0.300), 3)
    elif num_field == 7:
        if turn == 1:
            pygame.draw.circle(surface, color, (h*0.766, h*0.499), h*0.100, 3)
        elif turn == -1:
            pygame.draw.line(surface, color, (h*0.698, h*0.430), (h*0.835, h*0.568), 3)
            pygame.draw.line(surface, color, (h*0.835, h*0.434), (h*0.698, h*0.568), 3)
    elif num_field == 8:
        if turn == 1:
            pygame.draw.circle(surface, color, (h*0.766, h*0.766), h*0.100, 3)
        elif turn == -1:
            pygame.draw.line(surface, color, (h*0.698, h*0.698), (h*0.835, h*0.835), 3)
            pygame.draw.line(surface, color, (h*0.835, h*0.698), (h*0.698, h*0.835), 3)

pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
black = 0, 0, 0
background = 255, 192, 180
turn = 1
map(height, screen, black)
results = [0, 0, 0, 0, 0, 0, 0, 0, 0]
font = pygame.font.SysFont('Comic Sans MS', 30)
timer = 20
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #sys.exit()
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            poz = pygame.mouse.get_pos()
            num_field = check(height, poz)
            if results[num_field] == 0:
                draw_object(height, screen, black, turn)
                if turn == 1 and num_field != None:
                    results[num_field] = 1
                elif turn == -1 and num_field != None:
                    results[num_field] = -1


                if (results[0] == results[3] == results[6] == 1) or (results[1] == results[4] == results[7] == 1) or \
                    (results[2] == results[5] == results[8] == 1) or (results[0] == results[1] == results[2] == 1) or \
                    (results[3] == results[4] == results[5] == 1) or (results[6] == results[7] == results[8] == 1) or \
                    (results[0] == results[4] == results[8] == 1) or (results[2] == results[4] == results[6] == 1):
                        screen.blit(font.render("Wygrało kółko", False, (0, 0, 0)), (0, 0))
                elif (results[0] == results[3] == results[6] == -1) or (results[1] == results[4] == results[7] == -1) or \
                    (results[2] == results[5] == results[8] == -1) or (results[0] == results[1] == results[2] == -1) or \
                    (results[3] == results[4] == results[5] == -1) or (results[6] == results[7] == results[8] == -1) or \
                    (results[0] == results[4] == results[8] == -1) or (results[2] == results[4] == results[6] == -1):
                        screen.blit(font.render("Wygrał krzyżyk", False, (0, 0, 0)), (0, 0))


                turn = -turn





    pygame.display.flip()