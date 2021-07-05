import sys

import pygame
from pygame.constants import QUIT

from settings import Settings

class GameOfLife:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Game of Life")

        self.bg_colour = (self.settings.bg_colour)
    
    def run_game(self):
        """Start the main loop for the game"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_colour)
            pygame.display.flip()

if __name__ == '__main__':
    gl = GameOfLife()
    gl.run_game()