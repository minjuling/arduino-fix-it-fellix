from PIL import Image, ImageDraw, ImageFont
import numpy as np

class Window():
    def __init__(self, x, y):
        self.wd1 = Image.open('Img/window1-1.png')
        self.wd2 = Image.open('Img/window2-1.png')
        self.wd3 = Image.open('Img/window3-1.png')
        self.wd4 = Image.open('Img/window4-1.png')
        self.wd5 = Image.open('Img/window5-1.png')

        self.check = 0

        self.curr_x = x
        self.curr_y = y

        self.state

    
    def break_window(self):
        self.state = self.wd1

    def clean(self):
        self.check += 1
        if check == 1:
            self.state = self.wd2
        elif check == 2:
            self.state = self.wd3
        elif check ==3:
            self.state = self.wd4
        elif check ==4:
            self.state = self.wd5
        elif check == 5:
            return 1
        
        
