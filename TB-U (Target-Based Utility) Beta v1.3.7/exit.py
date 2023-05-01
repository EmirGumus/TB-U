
import pygame, sys
from settings import*

class Exit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(exit_image)
        self.rect = self.image.get_rect(topleft = (200,120))
    
    def exit(self):
        for exit in exit_group:
            tuple = exit.rect.center
            tupleminus = [exit.rect.centerx-100, exit.rect.centery-50]
            tupleplus = [exit.rect.centerx+100, exit.rect.centery+50]
            result1 = all(x <= y for x, y in zip(tupleminus, pygame.mouse.get_pos()))
            result2 = all(x >= y for x, y in zip(tupleplus, pygame.mouse.get_pos()))  
            if (result1 and result2) or tuple == pygame.mouse.get_pos(): 
                return True
