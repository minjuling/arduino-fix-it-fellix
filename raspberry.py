from PIL import Image, ImageDraw, ImageFont
import numpy as np

class Raspberry():
    def __init__(self):
        self.image = Image.open('Img/ras.png')

        self.curr_x = 10
        self.curr_y = 10

        self.next_x = np.random.randint(10, 150)
    
    def moving(self):
        if abs(self.curr_x-self.next_x) <= 11:
            self.next_x = np.random.randint(10, 150)
        elif self.curr_x>self.next_x:
            self.curr_x -= 10
        elif self.curr_x<self.next_x:
            self.curr_x += 10
        