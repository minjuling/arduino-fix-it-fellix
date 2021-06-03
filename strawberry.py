from PIL import Image, ImageDraw, ImageFont

class Strawberry():
    def __init__(self):
        self.img1 = Image.open('Img/st1.png')
        self.img2 = Image.open('Img/st2.png')
        self.img3 = Image.open('Img/st3.png')
        self.img4 = Image.open('Img/st4.png')
        self.img5 = Image.open('Img/st5.png')

        self.curr_x = 63
        self.curr_y = 30

        self.image = self.img1
    
    def up(self):
        if self.curr_y>-100:
            self.curr_y -= 30

    def down(self):
        if self.curr_y <30:
            self.curr_y += 10
        self.image = self.img1
    
    def left(self):
        if self.curr_x>-30:
            self.curr_x -= 10
        self.image = self.img2
    
    def right(self):
        if self.curr_x<163:
            self.curr_x += 10
        self.image = self.img3
        
    def A(self):
        if self.image == self.img2 or self.image == self.img5:
            self.image = self.img5
        else:
            self.image = self.img4