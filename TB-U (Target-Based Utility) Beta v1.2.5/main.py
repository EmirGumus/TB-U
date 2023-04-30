
import pygame
from gamestate import GameState
from settings import*

class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.game_state = GameState()
        
        pygame.display.set_caption(caption) #TODO achievement add
        pygame.display.set_icon(pygame.image.load(icon_image))

        pygame.mouse.set_visible(False)

    def run(self):
        while True:
            self.game_state.state_manager()
            self.clock.tick(FPS)

if __name__ == "__main__":
    game = Game()
    game.run()
