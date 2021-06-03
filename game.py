from PIL import Image, ImageDraw, ImageFont
import time

class Game():
    def __init__(self):
        self.img1 = Image.open('Img/background1.png')
        self.img2 = Image.open('Img/background2.png')
        self.img3 = Image.open('Img/background3.png')

        self.stage = [self.img1, self.img2, self.img3]
        self.check = 0

        self.image = self.stage[self.check]
        
        

    def change_stage(self,draw, image, disp):
            self.check += 1
            if self.check <3:
                draw.rectangle((0, 0, disp.width, disp.height), outline=0, fill=0)
                fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)
                draw.text((20, 110), "NEXT STAGE", font=fnt, fill=(255,255,255))
                disp.image(image)
                self.image = self.stage[self.check]
                time.sleep(2)

