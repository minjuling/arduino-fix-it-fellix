from PIL import Image, ImageDraw, ImageFont
import numpy as np

class Window():
    def __init__(self, x, y):
        self.wd1 = Image.open('Img/window1.png')
        self.wd2 = Image.open('Img/window2.png')
        self.wd3 = Image.open('Img/window3.png')
        self.wd4 = Image.open('Img/window4.png')
        self.wd5 = Image.open('Img/window5.png')

        #For correspoding image in the self.state
        self.check = 0
        #Image list
        self.state = [self.wd1, self.wd2, self.wd3, self.wd4, self.wd5]

        #Window position
        self.curr_x = x
        self.curr_y = y

        #Image in the self.state correspoding self.check idx
        self.image = self.state[self.check]


    def clean(self):
        self.check += 1
        if self.check<5:
            #change corresponding image
            self.image = self.state[self.check]
