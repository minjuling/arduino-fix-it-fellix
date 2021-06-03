from PIL import Image, ImageDraw, ImageFont

class Game():
    def __init__(self):
        self.img1 = Image.open('Img/background1.png')
        self.stage = self.img1
