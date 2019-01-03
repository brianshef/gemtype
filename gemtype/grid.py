import arcade
from random import randint

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
            for _ in range(self.column_count):
                self.grid[row].append(randint(0, 1))
    
    def draw(self):
        for row in range(self.row_count):
            for column in range(self.column_count):
                # Figure out what color to draw the box
                if self.grid[row][column] == 1:
                    color = (50, 200, 50, 70)
                else:
                    color = (30, 40, 50, 90)

                # Do the math to figure out where the box is
                x = (self.margin + self.cell_width) * column + self.margin + self.cell_width // 2
                y = (self.margin + self.cell_height) * row + self.margin + self.cell_height // 2

                # Draw the box
                arcade.draw_rectangle_filled(x, y, self.cell_width, self.cell_height, color)