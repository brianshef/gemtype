import arcade
from random import randint
from . import block

class Grid:
    def __init__(self, cell_width=50, cell_height=50, margin=1, screen_width=800, screen_height=600):
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.margin = margin
        self.row_count = int(screen_height / (cell_width + margin))
        self.column_count = int(screen_width / (cell_height + margin))
        self.grid = []
        for row in range(self.row_count):
            self.grid.append([])
            for column in range(self.column_count):
                b = block.Block(self.cell_width, self.margin, row, column, type=randint(0, 1))
                self.grid[row].append(b)
    
    def draw(self):
        for row in range(self.row_count):
            for column in range(self.column_count):
                self.grid[row][column].draw()
