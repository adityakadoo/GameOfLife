import sys

import pygame
from pygame.constants import QUIT

from settings import Settings
from cell import Cell

class GameOfLife:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init()
        self.settings = Settings()
        self.number_cells_x = int(input("Enter number of cells in a row: "))
        self.cell_width = float(self.settings.screen_width // self.number_cells_x)
        #print(self.cell_width)
        self.number_cells_y = int(self.settings.screen_height // self.cell_width)

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Game of Life")

        self.cells = pygame.sprite.Group()
        self._create_cells()

        self.bg_colour = (self.settings.bg_colour)
    
    def _create_cell(self,row_number,cell_number):
        """Creates a cell at given position"""
        cell = Cell(self)
        cell.x = cell_number * self.cell_width
        cell.y = row_number * self.cell_width
        cell.rect.x = cell.x
        cell.rect.y = cell.y
        self.cells.add(cell)

    def _create_cells(self):
        """Create all cells"""
        for row_number in range(self.number_cells_y):
            for cell_number in range(self.number_cells_x):
                self._create_cell(row_number,cell_number)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_event()
            self._update_screen()
    
    def _check_event(self):
        """Checks for input from keyboard and mouse"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.K_q:
                sys.exit()

    def _update_screen(self):
        """Update all the cells and the background"""
        self.screen.fill(self.bg_colour)
        for cell in self.cells.sprites():
            cell.draw_cell()
        
        pygame.display.flip()

if __name__ == '__main__':
    gl = GameOfLife()
    gl.run_game()