from PIL import Image, ImageDraw, ImageFont
import numpy as np

class Window():
    def __init__(self, x, y):
        self.wd1 = Image.open('Img/window1.png')
        self.wd2 = Image.open('Img/window2.png')
        self.wd3 = Image.open('Img/window3.png')
        self.wd4 = Image.open('Img/window4.png')
        self.wd5 = Image.open('Img/window5.png')

        self.check = 0
        self.state = [self.wd1, self.wd2, self.wd3, self.wd4, self.wd5]

        self.curr_x = x
        self.curr_y = y

        self.image = self.wd1


    def clean(self):
        self.check += 1
        if self.check<5:
            self.image = self.state[self.check]
