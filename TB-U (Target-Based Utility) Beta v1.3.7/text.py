
import pygame
from settings import*

class Text():
    def __init__(self):
        self.font_intro = pygame.font.Font(font1,200)
        self.text_intro = self.font_intro.render("Ready?",True,"Green")
        self.rect_itext = self.text_intro.get_rect(center = (960,540))
        
        self.font_score = pygame.font.Font(font2,75)
        self.text_main = self.font_score.render(score_show(),True, "Green")
        self.rect_mtext = self.text_main.get_rect(center = (1460,160))
