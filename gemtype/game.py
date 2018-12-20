import arcade

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height, 'GemType by Brian Shef')

        arcade.set_background_color(arcade.color.SLATE_GRAY)

    def setup(self):
        # Set up your game here
        pass

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        # Your drawing code goes here
        arcade.draw_text('Under construction', 20, SCREEN_HEIGHT - 40, arcade.color.WHITE, 22)

        # Finish drawing and display the result
        # arcade.finish_render()


    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        pass


def main():
    print ('Starting GemType ... ')
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()
    print (' ... closing GemType')
