from PIL import Image, ImageDraw, ImageFont
import numpy as np

class Raspberry():
    def __init__(self):
        self.ras1 = Image.open('Img/ras.png')
        self.ras2 = Image.open('Img/end1.png')
        self.ras3 = Image.open('Img/end2.png')
        self.ras4 = Image.open('Img/end3.png')


        self.image = self.ras1

        self.curr_x = 10
        self.curr_y = 10

        self.next_x = np.random.randint(10, 150)
    
    
    def moving(self):
        """
        move raspberry
        """

        #if raspberry position reach to next position
        if abs(self.curr_x-self.next_x) <= 6:
            #randomly set raspberry position
            self.next_x = np.random.randint(10, 150)
            
        #else if move raspberry position
        elif self.curr_x>self.next_x:
            self.curr_x -= 5
        elif self.curr_x<self.next_x:
            self.curr_x += 5
        