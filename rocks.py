import time
from PIL import Image, ImageDraw, ImageFont
from rock import Rock

class Rocks():
    def __init__(self):
        self.list = []
        self.next_t = 0
        self.curr_t = time.time()
        self.createtime = [5, 3, 2]


    #create rock
    def create_rock(self,x, y, stagenum):
        self.next_t = time.time()

        if stagenum<3 and abs(self.next_t-self.curr_t)>self.createtime[stagenum]:

            rock = Rock(x, y)
            self.list.append(rock)

            self.curr_t = time.time()
    
    #rock instance is reach floor, del this instance
    def rock_delete(self):
        self.list = [rock for rock in self.list if rock.moving() == 1]

    #rock instance is reach strawberry, return 1 for quit game
    def rock_check(self, x, y):
        for rock in self.list:
            if rock.check(x,y) == 1:
                return 1

    #rock moving
    def rock_moving(self):
        for rock in self.list:
            rock.moving()