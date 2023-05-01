
import pygame, sys, random
from settings import*
from exit import Exit
from crosshair import Crosshair
from target import Target
from text import Text

class GameState():
    def __init__(self):
        pygame.init()
        
        self.state = "intro"
        self.screen =  pygame.display.set_mode((WIDTH,HEIGTH))
        self.bg = pygame.image.load(bg_image)
        
        self.text = Text()
        
        self.exit = Exit()
        exit_group.add(self.exit)
        
        self.crosshair = Crosshair()
        crosshair_group.add(self.crosshair)
        
        for target in range(1):
            new_target = Target(random.randint(420,WIDTH-420), random.randint(155,HEIGTH-155))
            target_group.add(new_target)
    
    def intro(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.exit.exit() == True:
                    pygame.quit()
                    sys.exit()
                self.state = "main_game"
                break
            
        self.screen.blit(self.bg,(0,0))
        self.screen.blit(self.text.text_intro,self.text.rect_itext)
        exit_group.draw(self.screen)
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
                if self.exit.exit() == True:
                    pygame.quit()
                    sys.exit()
                
        self.text.text_main = self.text.font_score.render(score_show(),True, "Green")
        self.screen.blit(self.bg,(0,0))
        exit_group.draw(self.screen)
        target_group.draw(self.screen)
        self.screen.blit(self.text.text_main,self.text.rect_mtext)
        crosshair_group.draw(self.screen)
        crosshair_group.update()
        pygame.display.update()
        pygame.display.flip()
        
    def state_manager(self):
        if self.state == "intro":
            self.intro()
        if self.state == "main_game":
            self.main_game()
