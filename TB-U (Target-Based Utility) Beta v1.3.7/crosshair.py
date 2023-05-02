
import pygame, random
from settings import*
from target import*

class Crosshair(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(cross_image)
        self.rect = self.image.get_rect(center = pygame.mouse.get_pos())
        self.gunshot = pygame.mixer.Sound(gun_sound)
    def shoot(self,crosshair):
        self.gunshot.play()
        for t in target_group:
            tuple = t.rect.center
            tupleminus = [t.rect.centerx-30, t.rect.centery-30]
            tupleplus = [t.rect.centerx+30, t.rect.centery+30]
            result1 = all(x <= y for x, y in zip(tupleminus, pygame.mouse.get_pos()))
            result2 = all(x >= y for x, y in zip(tupleplus, pygame.mouse.get_pos()))  
            if (result1 and result2) or tuple == pygame.mouse.get_pos(): 
                pygame.sprite.spritecollide(crosshair, target_group, True)
                new_target = Target(random.randint(420,WIDTH-420), random.randint(155,HEIGTH-155))
                target_group.add(new_target)
                score_plus()
    def update(self):
        self.rect.center = pygame.mouse.get_pos()