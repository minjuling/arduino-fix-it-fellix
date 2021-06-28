#background(240x240)
#strawberry(40x45)
#raspberry(80x70)
#rocks(20x20)
#window(12x20)

from game import Game
from setting import Setting

#instance
game = Game()
setting = Setting()
berry, ras, windows, rocks = game.gameinit()

while True:

    #raspberry moving
    ras.moving()

    #rock moving
    rocks.rock_moving()

    #rock create every 3 second
    rocks.create_rock(ras.curr_x,ras.curr_y, game.stagecheck)
    
    #rock delete if it hit the floor
    rocks.rock_delete()

    # up pressed, berry up
    if not setting.button_U.value:  
        berry.up()
    
    # down pressed, berry down
    if not setting.button_D.value: 
        berry.down()
        
    # left pressed, berry left
    if not setting.button_L.value:
        berry.left()
    
    # right pressed, berry right
    if not setting.button_R.value:
        berry.right()

    # A pressed, fix window
    if not setting.button_A.value:  
        berry.A()
        windows.window_check(berry.curr_x, berry.curr_y) #window fix check

    #berry hit rock, game over
    if rocks.rock_check(berry.curr_x,berry.curr_y):
        game.gameover(setting.draw, setting.image, setting.disp)
    
    #if every window fix, next stage
    if len(windows.list) == 0:
        game.change_stage(setting.draw, setting.image, setting.disp)
        berry, ras, windows, rocks = game.gameinit()
        continue
    #else if last stage, ending
    elif game.stagecheck ==3:
        game.ending(berry, ras, setting.draw, setting.image, setting.disp)
        quit()
        
    # Display the Image
    setting.image.paste(game.image, (0,0))
    
    #every broken window display
    for window in windows.list:
        setting.image.paste(window.image, (window.curr_x,window.curr_y), window.image)
    #every rock display
    for rock in rocks.list:
        setting.image.paste(rock.image, (rock.curr_x,rock.curr_y), rock.image)
    
    setting.image.paste(ras.image, (ras.curr_x,ras.curr_y),ras.image)
    setting.image.paste(berry.image, (berry.curr_x, berry.curr_y),berry.image)
    setting.disp.image(setting.image)