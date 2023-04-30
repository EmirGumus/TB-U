
import pygame, sys, random
from settings import*
from crosshair import Crosshair
from target import Target

class GameState():
    def __init__(self):
        pygame.init()
        
        self.state = "intro"
        self.screen =  pygame.display.set_mode((WIDTH,HEIGTH))
        self.bg = pygame.image.load(bg_image)
        
        self.font = pygame.font.Font(font1,200)
        self.text_intro = self.font.render("Ready?",True,"Green")
        self.rect_text = self.text_intro.get_rect(center = (960,540))
        
        self.crosshair = Crosshair()
        crosshair_group.add(self.crosshair)
        
        for target in range(1):
            new_target = Target(random.randint(240,WIDTH-240), random.randint(155,HEIGTH-155))
            target_group.add(new_target)
    
    def intro(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = "main_game"
                break
            
        self.screen.blit(self.bg,(0,0))
        self.screen.blit(self.text_intro,self.rect_text)
        crosshair_group.draw(self.screen)
        crosshair_group.update()
        pygame.display.update()
        pygame.display.flip()

    def main_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.crosshair.shoot(self.crosshair)
                    
        pygame.display.update()
        pygame.display.flip()
        self.screen.blit(self.bg,(0,0))
        target_group.draw(self.screen)
        crosshair_group.draw(self.screen)
        crosshair_group.update()

    def state_manager(self):
        if self.state == "intro":
            self.intro()
        if self.state == "main_game":
            self.main_game()