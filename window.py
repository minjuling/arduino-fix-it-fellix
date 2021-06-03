from PIL import Image, ImageDraw, ImageFont
import numpy as np

class Window():
    def __init__(self):
        self.wd1 = Image.open('Img/window1-1.png')
        self.wd2 = Image.open('Img/window2-1.png')
        self.wd3 = Image.open('Img/window3-1.png')
        self.wd4 = Image.open('Img/window4-1.png')
        self.wd5 = Image.open('Img/window5-1.png')

        self.window_pose = []

        self.idx
        self.num

        self.clean = []
        self.check

    
    def break_window(self):
        self.idx = np.random.randint(0,8)
        self.num = len(self.idx)

        for i in self.idx:
            self.clean.append(self.window_pose[i])
        return self.clean, self.check
            
        
