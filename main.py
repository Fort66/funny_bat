import pygame, sys
# импортируем инициализацию
from intialization import *
from config import win, win_width, win_height, fps, background_img, current_living, orientation, gameplay     #, background_sound

# win = pygame.display.set_mode((1920, 1000)) 

fps_clock = pygame.time.Clock()

pygame.init()

bg_x = 0 # нач позиция фона

# background_sound.play()

while True:
    # win.fill((255, 255, 255))
    win.blit(background_img, (bg_x, 0))
    win.blit(background_img, (bg_x + win_width, 0))
    
    sprites.getSprite(*player.getSprite()).render(win, player.getPosition())

    npcs.draw(win)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        orientation = "L"
        # player.setState("left")
        player.setState(npcs.player_state(current_living, orientation))
        player.moveX(-SPEED_X)

    if keys[pygame.K_RIGHT]:
        orientation = "R"
        player.setState(npcs.player_state(current_living, orientation))
        player.moveX(SPEED_X)

    if keys[pygame.K_UP]:
        player.moveY(-SPEED_Y)

    if keys[pygame.K_DOWN]:
        player.moveY(SPEED_Y)
         
    npcs.update(player)                 

    bg_x -= 2
    if bg_x == - win_width:   
        bg_x = 0


    fps_clock.tick(fps)
    pygame.display.update()