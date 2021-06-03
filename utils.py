import numpy as np
import time
from PIL import Image, ImageDraw, ImageFont

from window import Window
from rock import Rock

def windowinit(window_position):
    breaknum = np.random.randint(0, 10)
    breakidx = np.random.randint(0, 10, breaknum)
    for i in breakidx:
        window = Window(window_position[i][1], window_position[i][2])
        window_list.append(window)
    return window_list

#make rock every 1sec
def make_rock(next_t, curr_t, rocks, x, y):
    if abs(next_t-curr_t)>3:
        rock = Rock(x, y)
        rocks.append(rock)
        curr_t = time.time()
    return rocks, curr_t

#rock instance is reach floor, del this instance
def rock_delete(rocks):
    rocks = [rock for rock in rocks if rock.moving() == 1]
    return rocks

#rock instance is reach strawberry, return 1 for quit game
def rock_check(rocks, x, y):
    for rock in rocks:
        if rock.check(x,y) == 1:
            return 1

#rock moving
def rock_moving(rocks):
    for rock in rocks:
        rock.moving()
    return rocks

def gameover(draw, image, disp):
    draw.rectangle((0, 0, disp.width, disp.height), outline=0, fill=0)
    fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)
    draw.text((30, 110), "GAME OVER", font=fnt, fill=(255,0,0))
    disp.image(image)
    quit()