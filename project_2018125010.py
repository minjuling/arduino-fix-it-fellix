
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Copyright (c) 2017 Adafruit Industries
# Author: James DeVito
# Ported to RGB Display by Melissa LeBlanc-Williams
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# This example is for use on (Linux) computers that are using CPython with
# Adafruit Blinka to support CircuitPython libraries. CircuitPython does
# not support PIL/pillow (python imaging library)!
"""
This example is for use on (Linux) computers that are using CPython with
Adafruit Blinka to support CircuitPython libraries. CircuitPython does
not support PIL/pillow (python imaging library)!
"""

import time
import random
from colorsys import hsv_to_rgb
import board
from digitalio import DigitalInOut, Direction
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789

# Create the display
cs_pin = DigitalInOut(board.CE0)
dc_pin = DigitalInOut(board.D25)
reset_pin = DigitalInOut(board.D24)
BAUDRATE = 24000000

spi = board.SPI()
disp = st7789.ST7789(
    spi,
    height=240,
    y_offset=80,
    rotation=180,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
)

# Input pins:
button_A = DigitalInOut(board.D5)
button_A.direction = Direction.INPUT

button_B = DigitalInOut(board.D6)
button_B.direction = Direction.INPUT

button_L = DigitalInOut(board.D27)
button_L.direction = Direction.INPUT

button_R = DigitalInOut(board.D23)
button_R.direction = Direction.INPUT

button_U = DigitalInOut(board.D17)
button_U.direction = Direction.INPUT

button_D = DigitalInOut(board.D22)
button_D.direction = Direction.INPUT

button_C = DigitalInOut(board.D4)
button_C.direction = Direction.INPUT

#image
background = Image.open('Img/background1.png')
ras = Image.open('Img/ras.png')
st1 = Image.open('Img/st1.png')
st2 = Image.open('Img/st2.png')
st3 = Image.open('Img/st3.png')
st4 = Image.open('Img/st4.png')
st5 = Image.open('Img/st5.png')
wd1 = Image.open('Img/window1-1.png')
wd2 = Image.open('Img/window2-1.png')
wd3 = Image.open('Img/window3-1.png')
wd4 = Image.open('Img/window4-1.png')
wd5 = Image.open('Img/window5-1.png')

# Turn on the Backlight
backlight = DigitalInOut(board.D26)
backlight.switch_to_output()
backlight.value = True

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for color.
width = disp.width
height = disp.height
image = Image.new("RGBA", (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Clear display.
draw.rectangle((0, 0, width, height), outline=0, fill=(255, 0, 0))
disp.image(image)

st_x = 63
st_y = 30
ras_x = 0
state = st1
check_x = random.randint(-60, 50)
#fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)
image.paste(state,(st_x,st_y))
    


while True:
    image.paste(background, (0,0))
    
    if abs(ras_x-check_x)<=11:
        check_x = random.randint(-60, 50)
    elif ras_x>check_x:
        ras_x -= 10
    elif ras_x<check_x:
        ras_x += 10
    print(ras_x, check_x)
    image.paste(ras, (ras_x,-10),ras)
    
    image.paste(state, (st_x,st_y),state) 
    
    if not button_U.value:  # up pressed
        if st_y >-100:
            st_y -= 30

     # Up
        

    if not button_D.value:  # down pressed
        if st_y <30:
            st_y += 30
        state = st1
 # down
        

    if not button_L.value:  # left pressed
        if st_x>-30:
            st_x -= 10
        state = st2
 # left
        

    if not button_R.value:  # right pressed
        if st_x<163:
            st_x +=10
        state = st3
 # right

        

    if not button_C.value:  # center pressed
        pass


    if not button_A.value:  # left pressed
        if state == st2:
            state = st5
        else:
            state = st4



    if not button_B.value:  # left pressed
        pass

    # make a random color and print text

#rcolor = tuple(int(x * 255) for x in hsv_to_rgb(random.random(), 1, 1))
    #draw.text((20, 150), "Hello World", font=fnt, fill=rcolor)
    #rcolor = tuple(int(x * 255) for x in hsv_to_rgb(random.random(), 1, 1))
    #draw.text((20, 180), "Hello World", font=fnt, fill=rcolor)
    #rcolor = tuple(int(x * 255) for x in hsv_to_rgb(random.random(), 1, 1))
    #draw.text((20, 210), "Hello World", font=fnt, fill=rcolor)

    # Display the Image
    disp.image(image)



