import pygame
from pygame.constants import WINDOWHITTEST
from pygame.sprite import Sprite

class Cell(Sprite):
    """A class to manage a single cell in the game"""

    def __init__(self,gl_game):
        """Initializes a pixel at top left corner"""
        super().__init__()
        self.screen = gl_game.screen
        self.screen_rect = self.screen.get_rect()
        self.cell_width = gl_game.cell_width
        self.settings = gl_game.settings
        self.colour = self.settings.cell_colour

        self.rect = pygame.Rect(0,0,self.cell_width,self.cell_width)
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.status = True
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    
    def update(self):
        """Update the status of a cell"""
        if self.status:
            self.status = False
        else:
            self.status = True
        if self.status:
            self.colour = self.settings.cell_colour
        else:
            self.colour = self.settings.bg_colour

    def draw_cell(self):
        """Draw the cell on the screen"""
        pygame.draw.rect(self.screen,self.colour,self.rect,1)