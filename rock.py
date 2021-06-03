import time
from PIL import Image, ImageDraw, ImageFont

class Rock():
    def __init__(self, rasp_x, rasp_y):
        self.image = Image.open('Img/rock.png')

        self.curr_x = rasp_x-70
        self.curr_y = rasp_y


    def moving(self):
        if self.curr_y>-240:
            self.curr_y -= 10
            return 1
        else: 
            return 0
            
    def check(self, x,y): 
        if abs(self.curr_x-x)<3 and abs(self.curr_y-y)<3:
            return 1
