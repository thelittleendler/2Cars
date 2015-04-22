__author__ = 'John Choo'

# _____________________________________ORDER OF CODE_____________________________________
# 1) DISPLAY
# 2) CAR
# 3) SQUARE
# 4) CIRCLE
# 5) COUNTER
# 6) CRASH INTO SQUARE
# 7) MOVEMENT LOOP
# 8) MAIN

import pygame
pygame.init()
pygame.font.init()
import time
import random
import os

# _____________________________________DISPLAY_____________________________________

# original 1080, 1920
display_width = 540
display_height = 960
ft = pygame.font.Font('freesansbold.ttf',60)

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

# _____________________________________CAR_____________________________________

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

# _____________________________________BACKGROUND_____________________________________

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

# _____________________________________SQUARE_____________________________________

SquareImageRed = pygame.image.load("C:\Users\John Choo\Desktop\eed.png")
SquareImageRed = pygame.transform.scale(SquareImageRed, (54, 54))

SquareImageBlue = pygame.image.load("C:\Users\John Choo\Desktop\eblue.png")
SquareImageBlue = pygame.transform.scale(SquareImageBlue, (54, 54))

square_redx = 183
square_redy = random.randint(-102, -42)
square_bluex = 320
square_bluey = random.randint(-42, 0)

def square_red(square_redx, square_redy):
    gameDisplay.blit(SquareImageRed, (square_redx, square_redy))

def square_blue(square_bluex, square_bluey):
    gameDisplay.blit(SquareImageBlue, (square_bluex, square_bluey))

def square_generator():
    global square_redx, square_redy, square_bluex, square_bluey
    square_redy += 3
    square_bluey += 3
    if square_redy > display_height:
        square_redy = random.randint(-202, -42)
        random.randint(1, 2)
        if random.randint(1, 2) == 1:
            square_redx = 47
        elif random.randint(1, 2) == 2:
            square_redx = 183
    if square_bluey > display_height:
        square_bluey = random.randint(-42, 0)
        random.randint(1, 2)
        if random.randint(1, 2) == 1:
            square_bluex = 320
        elif random.randint(1, 2) == 2:
            square_bluex = 451

    square_red(square_redx, square_redy)
    square_blue(square_bluex, square_bluey)


# _____________________________________CIRCLE_____________________________________

# circle properties
def circles(colour, origin, radius):
    pygame.draw.circle(gameDisplay, colour, origin, radius)

circle_redx = 72
circle_redy = ((random.randint(-55, -15))*3)-1
circle_bluex = 477
circle_bluey = ((random.randint(-55, -15))*3)-1

def red_circle():
    global circle_redy, circle_redx
    circles(red, (circle_redx, circle_redy), 26)
    circles(white, (circle_redx, circle_redy), 19)
    circles(red, (circle_redx, circle_redy), 13)

def blue_circle():
    global circle_bluey, circle_bluex
    circles(blue, (circle_bluex, circle_bluey), 26)
    circles(white, (circle_bluex, circle_bluey), 19)
    circles(blue, (circle_bluex, circle_bluey), 13)

def circle_generator():
    global circle_redy, circle_redx, circle_bluey, circle_bluex
    circle_redy += 3
    circle_bluey += 3
    if circle_redy > display_height + 150:
        circle_redy = ((random.randint(-55, 0))*3)-1
        random.randint(1, 2)
        if random.randint(1, 2) == 1:
            circle_redx = 72
        elif random.randint(1, 2) == 2:
            circle_redx = 206
    if circle_bluey > display_height + 150:
        circle_bluey = ((random.randint(-55, 0))*3)-1
        random.randint(1, 2)
        if random.randint(1, 2) == 1:
            circle_bluex = 347
        elif random.randint(1, 2) == 2:
            circle_bluex = 477

    red_circle()
    blue_circle()

# _____________________________________COUNTER_____________________________________

count = 0

# in charge of display only
def display_circles_hit(count):
    font = pygame.font.SysFont('freesansbold.ttf', 45)
    text = font.render(str(count), True, white)
    gameDisplay.blit(text, (465, 45))

# logic for counter only
red_passed = False
blue_passed = False

def counter():
    global count, red_passed, blue_passed, circle_redy, circle_bluey, xred, xblue

    if not red_passed:
        if (circle_redy + 26 == yred) and (circle_redx - 26) < (xred + 24) < (circle_redx + 26):
            count += 1
        if (circle_redy - 124 == yred) and (circle_redx - 26) < (xred + 24) < (circle_redx + 26):
            count += 1

    if not blue_passed:
        if (circle_bluey + 26 == yblue) and (circle_bluex - 26) < (xblue + 24) < (circle_bluex + 26):
            count += 1
        if (circle_bluey - 124 == yblue) and (circle_bluex - 26) < (xblue + 24) < (circle_bluex + 26):
            count += 1

# flag for counter
# contact can occur at top or BOTTOM
# to avoid "double count" for sensor at top and bottom we add a flag to activate/deactivate script

def red_passed_detector():
    global red_passed, circle_redy, circle_redx
    if (circle_redy + 23 == yred) and (circle_redx - 26) < (xred + 24) < (circle_redx + 26):
        red_passed = True
    if circle_redy == 101:
        red_passed = False

def blue_passed_detector():
    global blue_passed
    if (circle_bluey + 23 > yblue) and (circle_bluex - 26) < (xblue + 24) < (circle_bluex + 26):
        blue_passed = True
        # print(blue_passed)
    if circle_bluey == 101:
        blue_passed = False
        # print(blue_passed)

# _____________________________________CRASH INTO SQUARE_____________________________________
restart = 0

def crash():
    global square_redy, square_redx, startscreen_mode, game_mode, restart
    if (square_redy + 52 >= yred) and ((square_redx - 26) < (xred - 26) < (square_redx + 26) or (square_redx - 26) < xred < (square_redx + 26) or (square_redx - 26) < (xred + 26) < (square_redx + 26)):
        print(restart)
        restart = 1
        startscreen_mode = 1
        game_mode = 0

# _____________________________________MOVEMENT LOOP_____________________________________

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
        square_red(square_redx, square_redy)
        square_blue(square_bluex, square_bluey)
        # red_circle()
        xred_change += -3
        xred += xred_change
        print(xred)
        pygame.display.flip()
        clock.tick(180)
        if xred <= 45:
            keypress_redleft = False

    # red car turn right (x)
    while (xred < 178) and (keypress_redright is True):
        therealbackground()
        RedCar(xred, yred)
        BlueCar(xblue, yblue)
        square_red(square_redx, square_redy)
        square_blue(square_bluex, square_bluey)
        xred_change += 3
        xred += xred_change
        print(xred)
        pygame.display.flip()
        clock.tick(180)
        if xred >= 178:
            keypress_redright = False

    # blue car turn left (c)
    while (xblue > 318) and (keypress_blueleft is True):
        therealbackground()
        RedCar(xred, yred)
        BlueCar(xblue, yblue)
        square_red(square_redx, square_redy)
        square_blue(square_bluex, square_bluey)
        xblue_change += -3
        xblue += xblue_change
        print(xblue)
        pygame.display.flip()
        clock.tick(180)
        if xblue == 318:
            keypress_blueleft = False

    # blue car turn right (v)
    while (xblue < 450) and (keypress_blueright is True):
        therealbackground()
        RedCar(xred, yred)
        BlueCar(xblue, yblue)
        square_red(square_redx, square_redy)
        square_blue(square_bluex, square_bluey)
        xblue_change += 3
        xblue += xblue_change
        print(xblue)
        pygame.display.flip()
        clock.tick(180)
        if xblue == 450:
            keypress_redright = False

# _____________________________________MAIN_____________________________________

startscreen_mode = 1
game_mode = 0

def main():
    # # # # start screen mode
    global startscreen_mode, game_mode, restart
    while startscreen_mode == 1:

        pygame.event.pump()
        mx, my = pygame.mouse.get_pos()
        lc = pygame.mouse.get_pressed()[0]

        gameDisplay.fill(white)

        normal_i = ft.render('Start Game', 1, (0, 0, 0)), ft.size('Normal Mode')

        gameDisplay.blit(normal_i[0], (120, 100))
        if 70 < mx < 488 and 85 < my < 160:
            pygame.draw.rect(gameDisplay, (0, 0, 0), (280-normal_i[1][0]/2-10, 125-normal_i[1][1]/2-5,normal_i[1][0]+20,normal_i[1][1]+10),4)
            if lc:
                startscreen_mode = 0
                game_mode = 1

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.flip()

    # # # # game mode
    global xred, xred_change, yred, xblue, xblue_change, yblue
    global keypress_redleft, keypress_redright, keypress_blueleft, keypress_blueright
    global count, restart

    while game_mode == 1:
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

        # # background
        therealbackground()

        # # circles
        circle_generator()

        # score_counter
        red_passed_detector()
        blue_passed_detector()
        counter()
        display_circles_hit(count)

        # crash
        # crash()

        # # squares
        square_generator()

        # cars
        RedCar(xred, yred)
        BlueCar(xblue, yblue)

        pygame.display.update()
        clock.tick(90)

    if restart == 1:
        print('restart received')
        # startscreen_mode = 1
        # game_mode = 0

main()
if restart == 1:
    print('hihi')
    # startscreen_mode = 1
    # game_mode = 0
    # pygame.display.flip()
    # pygame.time.wait(20)
