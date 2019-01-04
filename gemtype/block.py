import arcade
from random import choice
from string import ascii_uppercase

FONT_SIZE = 32

class Block:
    def __init__(self, size, margin, row, column):
        self.size = size
        self.margin = margin
        self.row = row
        self.column = column
        self.x = (self.margin + self.size) * self.column + self.margin + self.size // 2
        self.y = (self.margin + self.size) * self.row + self.margin + self.size // 2
        self.center_x = self.x + self.size // 2
        self.center_y = self.y + self.size // 2
        self.color = (0, 0, 0, 0)
    
    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.size, self.size, self.color)



class AlphaBlock(Block):
    def __init__(self, size, margin, row, column):
        Block.__init__(self, size, margin, row, column)
        self.color = arcade.color.GREEN 
        self.text = choice(ascii_uppercase)

    def draw(self):
        Block.draw(self)
        arcade.draw_text(self.text,
                         self.x - self.size // 3.5,
                         self.center_y,
                         arcade.color.WHITE,
                         FONT_SIZE,
                         align="left", anchor_x="left", anchor_y="top")



class StoneBlock(Block):
    def __init__(self, size, margin, row, column):
        Block.__init__(self, size, margin, row, column)
        self.color = arcade.color.DIM_GRAY