import time
import random
from colorsys import hsv_to_rgb
import board
from digitalio import DigitalInOut, Direction
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789

from strawberry import Strawberry
from rock import Rock
from raspberry import Raspberry
from game import Game
from window import Window
import utils

# Create the display
cs_pin = DigitalInOut(board.CE0)
dc_pin = DigitalInOut(board.D25)
reset_pin = DigitalInOut(board.D24)
BAUDRATE = 24000000

spi = board.SPI()
disp = st7789.ST7789(
    spi,
    height=240,
    y_offset=80,
    rotation=180,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
)

# Input pins:
button_A = DigitalInOut(board.D5)
button_A.direction = Direction.INPUT

button_B = DigitalInOut(board.D6)
button_B.direction = Direction.INPUT

button_L = DigitalInOut(board.D27)
button_L.direction = Direction.INPUT

button_R = DigitalInOut(board.D23)
button_R.direction = Direction.INPUT

button_U = DigitalInOut(board.D17)
button_U.direction = Direction.INPUT

button_D = DigitalInOut(board.D22)
button_D.direction = Direction.INPUT

button_C = DigitalInOut(board.D4)
button_C.direction = Direction.INPUT

# Turn on the Backlight
backlight = DigitalInOut(board.D26)
backlight.switch_to_output()
backlight.value = True

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for color.
width = disp.width
height = disp.height
image = Image.new("RGBA", (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Clear display.
draw.rectangle((0, 0, width, height), outline=0, fill=0)
disp.image(image)

#instance
game = Game()
berry = Strawberry()
ras = Raspberry()
rocks = []
window_position = []
widow_list = []

curr_t = time.time()

while True:

    #raspberry moving
    ras.moving()

    #rock moving
    rocks = utils.rock_moving(rocks)

    #window break
    #utils.windowinit(window_position)

    #rock
    next_t = time.time()
    rocks, curr_t = utils.make_rock(next_t, curr_t, rocks, ras.curr_x,ras.curr_y )
    rocks = utils.rock_delete(rocks)

    

    if not button_U.value:  # up pressed
        berry.up()
        
    if not button_D.value:  # down pressed
        berry.down()
        
    if not button_L.value:  # left pressed
        berry.left()
        
    if not button_R.value:  # right pressed
        berry.right()

    if not button_C.value:  # center pressed
        pass

    if not button_A.value:  # left pressed
        berry.A()

    if not button_B.value:  # left pressed
        pass

    if utils.rock_check(rocks, berry.curr_x,berry.curr_y):
        utils.gameover(draw, image, disp)
    
    # Display the Image
    image.paste(game.stage, (0,0))
    image.paste(ras.image, (ras.curr_x,ras.curr_y),ras.image)
    image.paste(berry.image, (berry.curr_x, berry.curr_y),berry.image)
    
    for rock in rocks:
        image.paste(rock.image, (rock.curr_x,rock.curr_y), rock.image)
    disp.image(image)