import arcade
import os
import random
import glob
from string import ascii_uppercase
from . import ball
from . import explosion
from . import background
from . import grid

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
MOVEMENT_SPEED = 3
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

        self.ball = None
        self.explosions_list = None
        self.shapes = None
        self.grid = None

    def setup(self):
        arcade.set_background_color(arcade.color.DARK_SLATE_GRAY)

        # Shape lists
        self.shapes = arcade.ShapeElementList()
        self.shapes.append(background.get_new_background(SCREEN_WIDTH, SCREEN_HEIGHT))
        self.shapes.append(background.create_ceiling(SCREEN_WIDTH, SCREEN_HEIGHT))
        for s in background.create_stalactites(SCREEN_WIDTH, SCREEN_HEIGHT, STALACTITE_COUNT):
            self.shapes.append(s)
        
        # Game Grid
        self.grid = grid.Grid(screen_width=SCREEN_WIDTH, screen_height=SCREEN_HEIGHT)
        
        # Sprite lists
        self.explosions_list = arcade.SpriteList()

        # Pre-load the animation frames. We don't do this in the __init__ because it
        # takes too long and would cause the game to pause.
        self.explosion_texture_list = []
        for t in glob.glob('assets/explosion/purple_dust/explosion*.png'):
            self.explosion_texture_list.append(arcade.load_texture(t))

        # Misc objects
        self.ball = ball.Ball(SCREEN_WIDTH, SCREEN_HEIGHT, 50, 50, 0, 0, 15, arcade.color.MAGENTA)

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        self.shapes.draw()
        self.grid.draw()
        self.ball.draw()
        self.explosions_list.draw()

        arcade.draw_text(str(self.ball.position_x) + ' ' + str(self.ball.position_y), 20, SCREEN_HEIGHT - 48, arcade.color.WHITE, 32)

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        self.ball.update()
        self.explosions_list.update()
    
    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        try:
            letter = self.alphabet[str(key)]
            print('User pressed ' + letter + ' key')
            self.grid.get_positions_of_letter_block(letter)
        except Exception:
            pass
        if key == arcade.key.LEFT:
            self.ball.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.ball.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.ball.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.ball.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.SPACE:
            x = explosion.Explosion(self.explosion_texture_list)
            x.center_x = self.ball.position_x
            x.center_y = self.ball.position_y
            self.explosions_list.append(x)


    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball.change_y = 0


def main():
    print ('Starting GemType ... ')
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()
    print (' ... closing GemType')
