import arcade
from random import choice
from string import ascii_uppercase

FONT_SIZE = 32
TYPE = ['default', 'char', 'word']

class Block:
    def __init__(self, size, margin, row, column, type=0):
        self.size = size
        self.margin = margin
        self.row = row
        self.column = column
        self.type = TYPE[type]
        self.x = (self.margin + self.size) * self.column + self.margin + self.size // 2
        self.y = (self.margin + self.size) * self.row + self.margin + self.size // 2
        self.center_x = self.x + self.size // 2
        self.center_y = self.y + self.size // 2
        self.text = '' if self.type == TYPE[0] else choice(ascii_uppercase)
    
    def draw(self):
        draw_text = False
        color = (100, 120, 100, 50)
        if self.type == TYPE[1]:
            color = arcade.color.GREEN
            draw_text=True
        arcade.draw_rectangle_filled(self.x, self.y, self.size, self.size, color)
        if draw_text:
            arcade.draw_text(self.text,
                         self.x - self.size // 3.5, self.center_y, arcade.color.WHITE, FONT_SIZE,
                         align="left", anchor_x="left", anchor_y="top")
                         
        
