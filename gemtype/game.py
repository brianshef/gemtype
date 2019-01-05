import arcade
import os
import random
import glob
from string import ascii_uppercase
from . import explosion
from . import background
from . import grid

# Set how many rows and columns we will have
ROW_COUNT = 15
COLUMN_COUNT = 25

# This sets the SIZE (length of a side) of each grid cell
CELL_SIZE = 50

# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 4

# Do the math to figure out oiur screen dimensions
SCREEN_WIDTH = (CELL_SIZE + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (CELL_SIZE + MARGIN) * ROW_COUNT + MARGIN

# Game constants
STALACTITE_COUNT = 64
ALPHA_START = 97

pos = None


class Game(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height, 'GemType by Brian Shef')

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.alphabet = {}
        alpha_key = ALPHA_START
        for i in range(0, len(ascii_uppercase)):
            self.alphabet[str(alpha_key)] = ascii_uppercase[i]
            alpha_key += 1

        self.explosions_list = None
        self.shapes = None
        self.grid = None

    def setup(self):
        arcade.set_background_color(arcade.color.DARK_SLATE_GRAY)

        # Shape lists
        self.shapes = arcade.ShapeElementList()
        self.shapes.append(background.get_new_background(SCREEN_WIDTH, SCREEN_HEIGHT))
        self.shapes.append(background.create_ceiling(SCREEN_WIDTH, SCREEN_HEIGHT))
        
        # Game Grid
        self.grid = grid.Grid(
            cell_size=CELL_SIZE, margin=MARGIN,
            row_count=ROW_COUNT, column_count=COLUMN_COUNT,
            screen_width=SCREEN_WIDTH, screen_height=SCREEN_HEIGHT
        )
        
        # Sprite lists
        self.explosions_list = arcade.SpriteList()

        # Pre-load the animation frames. We don't do this in the __init__ because it
        # takes too long and would cause the game to pause.
        self.explosion_texture_list = []
        for t in glob.glob('assets/explosion/purple_dust/explosion*.png'):
            self.explosion_texture_list.append(arcade.load_texture(t))

        # Misc objects
        pass

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        self.shapes.draw()
        self.grid.draw()
        self.explosions_list.draw()

        arcade.draw_text('PRE-ALPHA', 16, SCREEN_HEIGHT - 16, (10, 10, 10, 120), 14)
        arcade.draw_text('PRE-ALPHA', 14, SCREEN_HEIGHT - 14, arcade.color.WHITE, 14)

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        self.explosions_list.update()
    
    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        pass

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        try:
            letter = self.alphabet[str(key)]
            print('User pressed ' + letter + ' key')
            positions = self.grid.get_positions_of_letter_block(letter)
            for p in positions:
                print('Going to explode @ ' + str(p) + ' ... ')
                self.explode(p)
        except Exception:
            pass
        if key == arcade.key.SPACE:
            self.explode()
    
    def explode(self, position=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)):
        """ Adds an explosion sprite animation at the supplied position """
        x = explosion.Explosion(self.explosion_texture_list)
        x.center_x = position[0]
        x.center_y = position[1]
        print('Exploding @ ' + str(position))
        self.explosions_list.append(x)


def main():
    print ('Starting GemType ... ')
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()
    print (' ... closing GemType')
