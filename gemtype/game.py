import arcade
import os
import random
from . import ball
from . import explosion

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
MOVEMENT_SPEED = 3
EXPLOSION_TEXTURE_COUNT = 160


class Game(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height, 'GemType by Brian Shef')
        self.ball = None
        self.explosions_list = None

    def setup(self):
        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        arcade.set_background_color(arcade.color.DARK_SLATE_GRAY)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)
        self.ball = ball.Ball(SCREEN_WIDTH, SCREEN_HEIGHT, 50, 50, 0, 0, 15, arcade.color.MAGENTA)

        # Sprite lists
        self.explosions_list = arcade.SpriteList()

        # Pre-load the animation frames. We don't do this in the __init__ because it
        # takes too long and would cause the game to pause.
        self.explosion_texture_list = []

        for i in range(EXPLOSION_TEXTURE_COUNT):
            # Files from http://www.explosiongenerator.com are numbered sequentially.
            # This code loads all of the explosion0000.png to explosion0270.png files
            # that are part of this explosion.
            texture_name = f"assets/explosion/purple_dust/explosion{i:04d}.png"

            self.explosion_texture_list.append(arcade.load_texture(texture_name))

        # self.explosions_list.preload_textures(self.explosion_texture_list)

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        # Your drawing code goes here
        arcade.draw_text('K A I A', 20, SCREEN_HEIGHT - 48, arcade.color.WHITE, 32)
        self.ball.draw()
        self.explosions_list.draw()

        # Finish drawing and display the result
        # arcade.finish_render()

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        self.ball.update()
        self.explosions_list.update()
    
    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
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
