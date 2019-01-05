import arcade
from random import randint

MAX_STALACTITE_WIDTH = 300
CEILING_HEIGHT = 100

# "Cavern" background decoration
def create_ceiling(max_width, max_height):
    color1 = (60, 60, 75, 255)
    color2 = (0, 0, 0, 0)
    points = (0, max_height), (max_width, max_height), (max_width, max_height-CEILING_HEIGHT), (0, max_height-CEILING_HEIGHT)
    colors = (color1, color1, color2, color2)
    return arcade.create_rectangles_filled_with_colors(points, colors)


# Main background

def get_new_background(max_width, max_height):
    color1 = rand_color()
    color2 = rand_color()
    points = (0, 0), (max_width, 0), (max_width, max_height), (0, max_height)
    colors = (color1, color1, color2, color2)
    return arcade.create_rectangles_filled_with_colors(points, colors)


def rand_color():
    return (rand_256(), rand_256(), rand_256())


def rand_256():
    return randint(0, 256)