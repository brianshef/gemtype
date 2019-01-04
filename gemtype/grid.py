import arcade
import glob
from random import randint, choice
from . import block

ALPHA_CHANCE = 10
MIN_ROW_BLOCK = 8

class Grid:
    def __init__(self, cell_width=50, cell_height=50, margin=1, screen_width=800, screen_height=600):
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.margin = margin
        self.row_count = int(screen_height / (cell_width + margin))
        self.column_count = int(screen_width / (cell_height + margin))
        self.grid = []
        self.stone_textures = glob.glob('assets/blocks/*.png')
        self.gem_textures = glob.glob('assets/gems/*.png')
            

        # Initialize the grid of blocks
        for row in range(self.row_count):
            self.grid.append([])
            for column in range(self.column_count):
                b = self.generate_block(row, column)
                self.grid[row].append(b)
    
    def draw(self):
        for row in range(self.row_count):
            for column in range(self.column_count):
                self.grid[row][column].draw()

    def generate_block(self, row, column):
        t = randint(0, 99)
        if t < ALPHA_CHANCE and row >= MIN_ROW_BLOCK:
            return block.AlphaBlock(self.cell_width, self.margin, row, column, texture_name=choice(self.gem_textures), back_texture_name=choice(self.stone_textures))
        elif row >= MIN_ROW_BLOCK:
            return block.StoneBlock(self.cell_width, self.margin, row, column, texture_name=choice(self.stone_textures))
        return block.Block(self.cell_width, self.margin, row, column)
