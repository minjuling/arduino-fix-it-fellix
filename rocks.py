import time
from PIL import Image, ImageDraw, ImageFont
from rock import Rock

class Rocks():
    """
    manage rock objects
    """
    def __init__(self):
        self.list = []
        self.curr_t = 0
        self.prev_t = time.time()
        
        #creation time according to stage
        self.createtime = [5, 3, 2]

    def manage_rock(self,x, y, stagenum):
        """
        create, move, delete rock
        """
        self.curr_t = time.time()

        #if stagenum is small than ending stage num and after a certain amount of time,
        #create rock object and set prev_t
        if stagenum<3 and abs(self.curr_t-self.prev_t)>self.createtime[stagenum]:

            rock = Rock(x, y)
            self.list.append(rock)

            self.prev_t = time.time()
        
        #move rock and rock object is reach floor, del this object
        self.list = [rock for rock in self.list if rock.moving(stagenum+1) == 0]
        

    
    def rock_check(self, x, y):
        """
        rock object is reach strawberry, 
        return 1 for quit game
        """
        for rock in self.list:
            return rock.check(x,y)