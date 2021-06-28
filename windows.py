from PIL import Image, ImageDraw, ImageFont
import numpy as np

from window import Window

class Windows():
    def __init__(self):
        self.list = []
        self.window_position = [[54,102],[81,102],[113,102],[146,102],[173,102],[54,152],[81,152],[146,152],[173,152],[54,200],[81,200],[146,200],[173,200]]
        
        breaknum = np.random.randint(6, 10)
        breakidx = np.random.randint(0, 10, breaknum)

        for i in breakidx:
            window = Window(self.window_position[i][0], self.window_position[i][1])
            self.list.append(window)

    def window_check(self,x,y):
        if len(self.list) ==0:
            return 0
        for window in self.list:
            if abs((window.curr_x+5) - (x+20))<10 and abs((window.curr_y+10) - (y+20))<5:
                window.clean()
                self.list = [window for window in self.list if window.check <5]
    
    
