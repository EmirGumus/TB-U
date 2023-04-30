
import pygame

#Main vars
FPS = 144
caption = "TB-U"
icon_image = "images/icon.png"

#GameState vars
WIDTH = 1920
HEIGTH =  1080
SCORE = 0
bg_image = "images/bg.png"
font1 = "fonts/joystix/joystix monospace.otf"
font2 = "fonts/press-start/prstartk.ttf"

#Crosshair vars
cross_image = "images/crosshair.png"
gun_sound = "sounds/gunshot.wav"
crosshair_group = pygame.sprite.Group()

#Target vars
target_image = "images/target.png"
target_group = pygame.sprite.Group()
