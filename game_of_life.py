import sys

import pygame
from pygame.constants import QUIT
from pygame.display import update

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

        self.cells = []
        self.to_be_updated = []
        self._create_cells()

        self.bg_colour = (self.settings.bg_colour)
        self.waiting = True
    
    def _create_cell(self,row_number,cell_number):
        """Creates a cell at given position"""
        cell = Cell(self)
        cell.x = cell_number * self.cell_width
        cell.y = row_number * self.cell_width
        cell.rect.x = cell.x
        cell.rect.y = cell.y
        return cell

    def _create_cells(self):
        """Create all cells"""
        for row_number in range(self.number_cells_y):
            row_cells = []
            row_to_be_updated = []
            for cell_number in range(self.number_cells_x):
                row_cells.append(self._create_cell(row_number,cell_number))
                row_to_be_updated.append(False)
            self.cells.append(row_cells)
            self.to_be_updated.append(row_to_be_updated)

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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    self.waiting = not self.waiting
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.waiting:
                    x,y = pygame.mouse.get_pos()
                    cell_addr_y = int(y/self.cell_width)
                    cell_addr_x = int(x/self.cell_width)
                    self.cells[cell_addr_y][cell_addr_x].update()

    def _get_neighbours(self,row_number,col_number):
        alive_neighbours = 0
        if row_number > 0:
            if self.cells[row_number-1][col_number].get_status():
                alive_neighbours += 1
        if row_number < self.number_cells_y -1:
            if self.cells[row_number+1][col_number].get_status():
                alive_neighbours += 1
        if col_number > 0:
            if self.cells[row_number][col_number-1].get_status():
                alive_neighbours += 1
        if col_number < self.number_cells_x -1:
            if self.cells[row_number][col_number+1].get_status():
                alive_neighbours += 1
        if row_number > 0 and col_number > 0:
            if self.cells[row_number-1][col_number-1].get_status():
                alive_neighbours += 1
        if row_number > 0 and col_number < self.number_cells_x -1:
            if self.cells[row_number-1][col_number+1].get_status():
                alive_neighbours += 1
        if row_number < self.number_cells_y -1 and col_number > 0:
            if self.cells[row_number+1][col_number-1].get_status():
                alive_neighbours += 1
        if row_number < self.number_cells_y -1 and col_number < self.number_cells_x -1:
            if self.cells[row_number+1][col_number+1].get_status():
                alive_neighbours += 1
        return alive_neighbours

    def _check_cells(self):
        """Ckeck for all the cells that need to be updated once the game starts"""
        for row_number in range(self.number_cells_y):
            for col_number in range(self.number_cells_x):
                alive_neighbours = self._get_neighbours(row_number,col_number)
                
                self.to_be_updated[row_number][col_number] = False
                if self.cells[row_number][col_number].get_status():
                    if alive_neighbours < 2:
                        self.to_be_updated[row_number][col_number] = True
                    elif alive_neighbours > 3:
                        self.to_be_updated[row_number][col_number] = True
                else:
                    if alive_neighbours == 3:
                        self.to_be_updated[row_number][col_number] = True

    def _update_cells(self):
        """Update cells once the game starts"""
        for row_number in range(self.number_cells_y):
            for col_number in range(self.number_cells_x):
                if self.to_be_updated[row_number][col_number]:
                    self.cells[row_number][col_number].update()

    def _update_screen(self):
        """Update all the cells and the background"""
        self.screen.fill(self.bg_colour)

        if not self.waiting:
            self._check_cells()
            self._update_cells()
        for row in self.cells:
            for cell in row:
                cell.draw_cell()
        
        pygame.display.flip()

if __name__ == '__main__':
    gl = GameOfLife()
    gl.run_game()