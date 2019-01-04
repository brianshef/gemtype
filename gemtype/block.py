import arcade
from random import choice
from string import ascii_uppercase

FONT_SIZE = 28
SPRITE_SCALING = 0.40

class Block:
    def __init__(self, size, margin, row, column, texture_name=None):
        self.id = str(row) + str(column)
        self.size = size
        self.margin = margin
        self.row = row
        self.column = column
        # Center coordinates
        self.x = (self.margin + self.size) * self.column + self.margin + self.size // 2
        self.y = (self.margin + self.size) * self.row + self.margin + self.size // 2
        self.color = (0, 0, 0, 0)
        self.sprite = None
        self.back_sprite = None
        if texture_name is not None:
            self.sprite = arcade.Sprite(
                texture_name, SPRITE_SCALING,
                image_height=128, image_width=128,
                center_x=self.x, center_y=self.y
            )
    
    def draw(self):
        if self.sprite is None and self.back_sprite is None:
            arcade.draw_rectangle_filled(self.x, self.y, self.size, self.size, self.color)
        else:
            if self.back_sprite is not None:
                self.back_sprite.draw()
            if self.sprite is not None:
                self.sprite.draw()



class AlphaBlock(Block):
    def __init__(self, size, margin, row, column, texture_name=None, back_texture_name=None):
        Block.__init__(self, size, margin, row, column, texture_name)
        self.color = arcade.color.GREEN 
        self.text = choice(ascii_uppercase)
        if texture_name is not None:
            self.sprite = arcade.Sprite(
                texture_name, 0.65,
                image_height=128, image_width=128,
                center_x=self.x, center_y=self.y
            )
        if back_texture_name is not None:
            self.back_sprite = arcade.Sprite(
                back_texture_name, SPRITE_SCALING,
                image_height=128, image_width=128,
                center_x=self.x, center_y=self.y
            )

    def draw(self):
        Block.draw(self)
        arcade.draw_text(self.text,
                         start_x=self.x, start_y=self.y,
                         color=(10, 10, 10, 135),
                         font_size=FONT_SIZE,
                         align="center",
                         anchor_x="center", anchor_y="center")



class StoneBlock(Block):
    def __init__(self, size, margin, row, column, texture_name=None):
        Block.__init__(self, size, margin, row, column, texture_name)
        self.color = arcade.color.DIM_GRAY
