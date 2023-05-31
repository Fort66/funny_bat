import pygame

win_width = 1920
win_height = 1000
win = pygame.display.set_mode((win_width, win_height))

fps = 30

start_living_hero = 100
current_living = 100
orientation = "R"

gameplay = True


background_img = pygame.image.load("./images/background/background.png").convert_alpha()
# background_sound = pygame.mixer.Sound("./sounds/nature.mp3")
