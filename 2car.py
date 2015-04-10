__author__ = 'John Choo'

# ORDER OF CODE
# 1) BACKGROUND
# 2) SQUARE
# 3) CIRCLE
# 4) MOVEMENT LOOP
# 5) MAIN

import pygame
pygame.init()
import time
import random
import os

# # # # BACKGROUND # # # #
# original 1080, 1920
display_width = 540
display_height = 960

# colour selection list
black = (0, 0, 0)
white = (255, 254, 255)
grey = (102, 102, 102)
whiteGrey = (204, 204, 204)
backgroundBlue = (35, 52, 122)
dividerBlue = (129, 151, 236)
red = (229, 54, 88)
blue = (79, 187, 235)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('2 Car')
clock = pygame.time.Clock()

# carImageRed = pygame.image.load("~Graphics\ed-car.png")
# carImageRed = pygame.image.load(os.path.join(os.path.expanduser("~\PycharmProjects\;2Car"), "Graphics\ed-car.png"))
carImageRed = pygame.image.load(os.path.join(os.path.join(os.curdir, 'Graphics'), "ed-car.png") )
carImageRed = pygame.transform.scale(carImageRed, (54, 96))

# carImageBlue = pygame.image.load("~Graphics\lue_car-v3.png")
carImageBlue = pygame.image.load(os.path.join(os.path.join(os.curdir, 'Graphics'), "lue_car-v3.png") )
carImageBlue = pygame.transform.scale(carImageBlue, (54, 96))

xred = 45
xred_change = 0
yred = 820
xblue = 450
xblue_change = 0
yblue = 820

def RedCar(xred, yred):
    gameDisplay.blit(carImageRed, (xred, yred))

def BlueCar(xblue, yblue):
    gameDisplay.blit(carImageBlue, (xblue, yblue))

# # # # BACKGROUND # # # #
def background():
    gameDisplay.fill(backgroundBlue)

# background line properties
def backgroundline(linex, liney, linew, lineh, color):
    pygame.draw.rect(gameDisplay, color, [linex, liney, linew, lineh])

# background combining both background blue and lines
def therealbackground():
    background()
    backgroundline(135, 0, 8.571, 2000, dividerBlue)
    backgroundline((display_width - 135), 0, 8.571, 2000, dividerBlue)
    backgroundline((display_width/2), 0, 17.142, 2000, dividerBlue)

# # # # SQUARE # # # #
SquareImageRed = pygame.image.load("C:\Users\John Choo\Desktop\eed.png")
SquareImageBlue = pygame.image.load("C:\Users\John Choo\Desktop\eblue.png")

square_redx = 206
square_redy = random.randint(-82, -62)
square_bluex = 344
square_bluey = random.randint(-82, -62)

def square_red(square_redx, square_redy):
    gameDisplay.blit(SquareImageRed, (square_redx, square_redy))

def square_blue(square_bluex, square_bluey):
    gameDisplay.blit(SquareImageBlue, (square_bluex, square_bluey))

def square_generator():
    global square_redx, square_redy, square_bluex, square_bluey
    square_redy += 3
    square_bluey += 3
    if square_redy > display_height:
        square_redy = 0
        random.randint(1, 2)
        if random.randint(1, 2) == 2:
            square_redx = 206
        elif random.randint(1, 2) == 1:
            square_redx = 72

    square_red()
    square_blue()


# # # # CIRCLE # # # #
# circle properties
def circles(colour, origin, radius):
    pygame.draw.circle(gameDisplay, colour, origin, radius)

circle_y = random.randint(-52, -32)
circle_redx = 72
circle_bluex = 477

def red_circle():
    global circle_y, circle_redx
    circles(red, (circle_redx, circle_y), 26)
    circles(white, (circle_redx, circle_y), 19)
    circles(red, (circle_redx, circle_y), 13)

def blue_circle():
    global circle_y, circle_bluex
    circles(blue, (circle_bluex, circle_y), 26)
    circles(white, (circle_bluex, circle_y), 19)
    circles(blue, (circle_bluex, circle_y), 13)

def circle_generator():
    global circle_y, circle_redx, circle_bluex
    circle_y += 3
    if circle_y > display_height:
        circle_y = 0
        random.randint(1, 2)
        if random.randint(1, 2) == 2:
            circle_redx = 206
        elif random.randint(1, 2) == 1:
            circle_redx = 72
        random.randint(3, 4)
        if random.randint(3, 4) == 3:
            circle_bluex = 344
        elif random.randint(3, 4) == 4:
            circle_bluex = 477

    red_circle()
    blue_circle()

# for circles_hit
# count = 0

# def circles_hit(count):
#     font = pygame.font.SysFont(None, 25)
#     text = font.render(str(count), True, white)
#     gameDisplay.blit(text, (450, 50))

# # # # MOVEMENT LOOP # # # #
keypress_redleft = False
keypress_redright = False
keypress_blueleft = False
keypress_blueright = False

def movement_loop():
    global xred, xred_change, yred, xblue, xblue_change, yblue
    global keypress_redleft, keypress_redright, keypress_blueleft, keypress_blueright

    # red car turn left (z)
    while (xred > 45) and (keypress_redleft is True):
        therealbackground()
        RedCar(xred, yred)
        BlueCar(xblue, yblue)
        xred_change += -3
        xred += xred_change
        print(xred)
        pygame.display.flip()
        pygame.time.delay(20)
        clock.tick(180)
        if xred == 45:
            keypress_redleft = False

    # red car turn right (x)
    while (xred < 150) and (keypress_redright is True):
        therealbackground()
        RedCar(xred, yred)
        BlueCar(xblue, yblue)
        xred_change += 3
        xred += xred_change
        print(xred)
        pygame.display.flip()
        pygame.time.delay(20)
        clock.tick(180)
        if xred == 150:
            keypress_redright = False

    # blue car turn left (c)
    while (xblue > 345) and (keypress_blueleft is True):
        therealbackground()
        RedCar(xred, yred)
        BlueCar(xblue, yblue)
        xblue_change += -3
        xblue += xblue_change
        print(xblue)
        pygame.display.flip()
        pygame.time.delay(20)
        clock.tick(180)
        if xblue == 345:
            keypress_blueleft = False

    # blue car turn right (v)
    while (xblue < 450) and (keypress_blueright is True):
        therealbackground()
        RedCar(xred, yred)
        BlueCar(xblue, yblue)
        xblue_change += 3
        xblue += xblue_change
        print(xblue)
        pygame.display.flip()
        pygame.time.delay(20)
        clock.tick(180)
        if xblue == 450:
            keypress_redright = False

# # # # MAIN # # # #
def main():
    gameExit = False
    global xred, xred_change, yred, xblue, xblue_change, yblue
    global keypress_redleft, keypress_redright, keypress_blueleft, keypress_blueright

    while not gameExit:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    keypress_redleft = True
                    movement_loop()
                elif event.key == pygame.K_x:
                    keypress_redright = True
                    movement_loop()
                elif event.key == pygame.K_c:
                    keypress_blueleft = True
                    movement_loop()
                elif event.key == pygame.K_v:
                    keypress_blueright = True
                    movement_loop()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_z or event.key == pygame.K_x or event.key == pygame.K_c or event.key == pygame.K_v:
                    keypress_redright = False
                    keypress_redleft = False
                    xred_change = 0
                    keypress_blueleft = False
                    keypress_blueright = False
                    xblue_change = 0

        xred += xred_change
        xblue += xblue_change

        # background
        therealbackground()

        # circles
        # circle_generator()

        # squares
        square_generator()

        # cars
        RedCar(xred, yred)
        BlueCar(xblue, yblue)

        pygame.display.update()
        clock.tick(90)


main()
pygame.quit()
quit()
