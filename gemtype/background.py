import arcade
from random import randint

def get_new_background(width, height):
    color1 = rand_color()
    color2 = rand_color()
    points = (0, 0), (width, 0), (width, height), (0, height)
    colors = (color1, color1, color2, color2)
    return arcade.create_rectangles_filled_with_colors(points, colors)


def rand_color():
    return (rand_256(), rand_256(), rand_256())


def rand_256():
    return randint(0, 256)