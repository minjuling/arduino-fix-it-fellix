from PIL import Image, ImageDraw, ImageFont
import numpy as np

from window import Window

class Windows():
    """
    manage window objects
    """
    def __init__(self):
        """
        Create broken window to random number at random location
        """

        #List for saving broken window instances
        self.list = []
        #Window position list
        self.window_position = [[54,102],[81,102],[113,102],[146,102],[173,102],[54,152],[81,152],[146,152],[173,152],[54,200],[81,200],[146,200],[173,200]]
        
        #Number of broken window
        breaknum = np.random.randint(6, 10)
        #Randomly pick window
        breakidx = np.random.randint(0, 13, breaknum)

        for i in breakidx:
            #create window object
            window = Window(self.window_position[i][0], self.window_position[i][1])
            #add window object to list
            self.list.append(window)

    def window_check(self,x,y):
        for window in self.list:
            #If strawberry is on the window
            if abs((window.curr_x+5) - (x+20))<10 and abs((window.curr_y+10) - (y+20))<5:
                #window clean
                window.clean()

        #When window is not comletely clean, left it in list
        self.list = [window for window in self.list if window.check <5]
    
    
