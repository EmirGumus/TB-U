
import pygame
from settings import*

class Target(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(target_image)
        self.rect = self.image.get_rect(center = (pos_x, pos_y))
