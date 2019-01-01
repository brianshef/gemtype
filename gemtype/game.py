import arcade
from . import ball

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
MOVEMENT_SPEED = 3


class Game(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height, 'GemType by Brian Shef')

        arcade.set_background_color(arcade.color.SLATE_GRAY)

    def setup(self):
        # Set up your game here
        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)
        self.ball = ball.Ball(SCREEN_WIDTH, SCREEN_HEIGHT, 50, 50, 0, 0, 15, arcade.color.MAGENTA)
        pass

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        # Your drawing code goes here
        arcade.draw_text('Under construction', 20, SCREEN_HEIGHT - 40, arcade.color.WHITE, 22)
        self.ball.draw()

        # Finish drawing and display the result
        # arcade.finish_render()

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        self.ball.update()
    
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
