from game import Game
from setting import Setting

#game initialization
game = Game()
setting = Setting()
berry, ras, windows, rocks = game.gameinit()

while True:

    ras.moving()
    rocks.create_rock(ras.curr_x,ras.curr_y, game.stagecheck)
    rocks.manage_rock(game.stagecheck+1)

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

    
    if len(windows.list) == 0:
        #set next stage
        game.change_stage(setting.draw, setting.image, setting.disp)
        #initialize game
        berry, ras, windows, rocks = game.gameinit()
        continue

    #else if last stage, end game
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