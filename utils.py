import numpy as np
import time
from PIL import Image, ImageDraw, ImageFont

from strawberry import Strawberry
from rock import Rock
from raspberry import Raspberry
from window import Window

def gameinit():
    berry = Strawberry()
    ras = Raspberry()

    window_position = [[54,102],[81,102],[113,102],[146,102],[173,102],[54,152],[81,152],[146,152],[173,152],[54,200],[81,200],[146,200],[173,200]]
    windows = windowinit(window_position)
    
    curr_t = time.time()

    rocks = []

    return berry, ras, window_position, windows, curr_t, rocks

def windowinit(window_position):
    breaknum = np.random.randint(6, 10)
    breakidx = np.random.randint(0, 10, breaknum)
    windows = []
    for i in breakidx:
        window = Window(window_position[i][0], window_position[i][1])
        windows.append(window)
    return windows

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

def window_check(windows,x,y):
    if len(windows) ==0:
        return 0
    for window in windows:
        if abs((window.curr_x+5) - (x+20))<10 and abs((window.curr_y+10) - (y+20))<5:
            window.clean()
            windows = [window for window in windows if window.check <5]
    return windows

def ending(berry, ras, draw, game,image, disp):

    draw.rectangle((0, 0, disp.width, disp.height), outline=0, fill=0)
    fnt1 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)
    fnt2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
    draw.text((30, 110), "YOU WIN!", font=fnt1, fill=(255,0,0))
    disp.image(image)
    time.sleep(0.5)


    image.paste(game.image, (0,0))
    image.paste(ras.ras2, (80,10),ras.ras2)

    for i in range(0,4):
        

        image.paste(game.image, (0,0))
        image.paste(ras.ras2, (80,10),ras.ras2)
        image.paste(berry.img1, (berry.curr_x, berry.curr_y),berry.img1)
        disp.image(image)
        time.sleep(1)
        image.paste(game.image, (0,0))
        image.paste(ras.ras2, (80,10),ras.ras2)
        image.paste(berry.img0, (berry.curr_x, berry.curr_y),berry.img0)
        disp.image(image)
        time.sleep(1)

    x = 10
    for i in range(0,4):
        image.paste(game.image, (0,0))
        image.paste(ras.ras2, (80,10),ras.ras2)
        image.paste(berry.img1, (x, 40),berry.img1)
        disp.image(image)
        x+=10
        time.sleep(0.5)
    
    image.paste(game.image, (0,0))
    image.paste(ras.ras2, (80,10),ras.ras2)
    image.paste(berry.img3, (60, 40),berry.img3)
    disp.image(image)
    time.sleep(0.5)
    
    ras_y = 10
    for i in range(1,6):
        ras_y += 30
        image.paste(game.image, (0,0))
        image.paste(berry.img3, (60, 40),berry.img3)
        image.paste(ras.ras2, (80, ras_y),ras.ras2)
        disp.image(image)
        time.sleep(0.5)


    ras_y = 10
    for i in range(1,6):
        ras_y += 30
        image.paste(game.img2, (0,0))
        image.paste(ras.ras2, (80, ras_y),ras.ras2)
        disp.image(image)
        time.sleep(0.5)

    image.paste(game.img3, (0,0))
    ras_y = 10
    for i in range(1,6):
        ras_y += 30
        image.paste(game.img1, (0,0))
        image.paste(ras.ras2, (80, ras_y),ras.ras2)
        disp.image(image)
        time.sleep(0.5)
    
    image.paste(ras.ras3, (0,0),ras.ras3)
    disp.image(image)
    time.sleep(1)

    image.paste(ras.ras4, (0,0),ras.ras4)
    disp.image(image)
    time.sleep(1)

    draw.rectangle((0, 0, disp.width, disp.height), outline=0, fill=0)
    
    draw.text((10, 80), "Thx for playing", font=fnt1, fill=(255,255,255))
    draw.text((20, 120), "made by minjuling", font=fnt2, fill=(255,255,255))
    disp.image(image)


  
