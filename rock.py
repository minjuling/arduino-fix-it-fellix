from PIL import Image, ImageDraw, ImageFont

class Rock():
    def __init__(self, rasp_x, rasp_y):
        self.image = Image.open('Img/rock.png')

        self.curr_x = rasp_x
        self.curr_y = rasp_y

        self.width = 20
        self.height = 20

    #move curr_y+1 and when reach floor, return 1
    def moving(self, stagenum):
        delete = 1
        if self.curr_y<240:
            self.curr_y += stagenum
            delete = 0
        return delete
    
    #When strawberry touch rock, return 1
    def check(self, x,y): 
        ch = 0
        if abs((self.curr_x+10)-(x+20))<20 and abs((self.curr_y+self.height)-(y+10))<3:
            ch = 1
        return ch
