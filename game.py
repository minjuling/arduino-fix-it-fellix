from PIL import Image, ImageDraw, ImageFont
import time

from strawberry import Strawberry
from rocks import Rocks
from raspberry import Raspberry
from windows import Windows

class Game():
    """
    Control game
    """
    def __init__(self):
        self.img1 = Image.open('Img/background1.png')
        self.img2 = Image.open('Img/background2.png')
        self.img3 = Image.open('Img/background3.png')

        #Stage image list
        self.stage = [self.img1, self.img2, self.img3]
        #Stage number
        self.stagenum = 0

        #Image in stage list correspoding to self.stagenum
        self.image = self.stage[self.stagenum]


    def gameinit(self):

        berry = Strawberry()
        ras = Raspberry()
        rocks = Rocks()
        windows = Windows()

        return berry, ras, windows, rocks
        

    def change_stage(self,draw, image, disp):
        
        self.stagenum += 1

        if self.stagenum <3:
            #change stage number
            self.image = self.stage[self.stagenum]

            #display NEXT STAGE text
            draw.rectangle((0, 0, disp.width, disp.height), outline=0, fill=0)
            fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)
            draw.text((20, 110), "NEXT STAGE", font=fnt, fill=(255,255,255))
            disp.image(image)
            time.sleep(2)


    def gameover(self, draw, image, disp):
        
        #display GAME OVER text
        draw.rectangle((0, 0, disp.width, disp.height), outline=0, fill=0)
        fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)
        draw.text((30, 110), "GAME OVER", font=fnt, fill=(255,0,0))
        disp.image(image)
        quit()


    def ending(self,berry, ras, draw, image, disp):
        
        #display YOU WIN text
        draw.rectangle((0, 0, disp.width, disp.height), outline=0, fill=0)
        fnt1 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)
        fnt2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
        draw.text((50, 110), "YOU WIN!", font=fnt1, fill=(255,0,0))
        disp.image(image)
        time.sleep(0.5)

        #display embarrassed raspberry image
        image.paste(self.image, (0,0))
        image.paste(ras.ras2, (80,10),ras.ras2)

        #display jumping strawberry 
        for i in range(0,4):
            
            image.paste(self.image, (0,0))
            image.paste(ras.ras2, (80,10),ras.ras2)
            image.paste(berry.img1, (berry.curr_x, berry.curr_y),berry.img1)
            disp.image(image)
            time.sleep(0.5)
            image.paste(self.image, (0,0)) 
            image.paste(ras.ras2, (80,10),ras.ras2)
            image.paste(berry.img0, (berry.curr_x, berry.curr_y),berry.img0)
            disp.image(image)
            time.sleep(0.5)

        #display moving strawberry to raspberry
        berry_x = 10
        for i in range(0,4):
            image.paste(self.image, (0,0))
            image.paste(ras.ras2, (80,10),ras.ras2)
            image.paste(berry.img1, (berry_x, 40),berry.img1)
            disp.image(image)
            berry_x+=10
            time.sleep(0.5)
        
        #display push raspberry
        image.paste(self.image, (0,0))
        image.paste(ras.ras2, (80,10),ras.ras2)
        image.paste(berry.img3, (60, 40),berry.img3)
        disp.image(image)
        time.sleep(0.5)
        
        #display raspberry falling in stage3 
        ras_y = 0
        for i in range(1,6):
            ras_y += 30
            image.paste(self.image, (0,0))
            image.paste(berry.img3, (60, 40),berry.img3)
            image.paste(ras.ras2, (80, ras_y),ras.ras2)
            disp.image(image)
            time.sleep(0.5)

        #display raspberry falling in stage2
        ras_y = 0
        for i in range(1,6):
            ras_y += 30
            image.paste(self.img2, (0,0))
            image.paste(ras.ras2, (80, ras_y),ras.ras2)
            disp.image(image)
            time.sleep(0.5)

        #display raspberry falling in stage1
        ras_y = 0
        for i in range(1,6):
            ras_y += 30
            image.paste(self.img1, (0,0))
            image.paste(ras.ras2, (80, ras_y),ras.ras2)
            disp.image(image)
            time.sleep(0.5)
        
        #display pop raspberry
        image.paste(ras.ras3, (0,0),ras.ras3)
        disp.image(image)
        time.sleep(1)

        image.paste(ras.ras4, (0,0),ras.ras4)
        disp.image(image)
        time.sleep(1)

        #display Thank you! text
        draw.rectangle((0, 0, disp.width, disp.height), outline=0, fill=0)
        
        draw.text((10, 80), "Thx for playing", font=fnt1, fill=(255,255,255))
        draw.text((20, 120), "made by minjuling", font=fnt2, fill=(255,255,255))
        disp.image(image)