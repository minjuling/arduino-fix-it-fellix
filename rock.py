import time
from PIL import Image, ImageDraw, ImageFont

class Rock():
    def __init__(self, rasp_x, rasp_y):
        self.image = Image.open('Img/rock.png')

        self.curr_x = rasp_x
        self.curr_y = rasp_y

        self.width = 20
        self.height = 20

    def moving(self):
        if self.curr_y<240:
            self.curr_y += 1
            return 1
        else: 
            return 0
            
    def check(self, x,y): 
        if abs((self.curr_x+10)-(x+20))<20 and abs((self.curr_y+self.height)-(y+10))<3:
            return 1
