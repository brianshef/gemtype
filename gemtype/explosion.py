import arcade


BULLET_SPEED = 5

EXPLOSION_TEXTURE_COUNT = 60


class Explosion(arcade.Sprite):
    """ This class creates an explosion animation """

    # Static variable that holds all the explosion textures
    explosion_textures = []

    def __init__(self, texture_list):
        super().__init__("assets/explosion/purple_dust/explosion0000.png")

        # Start at the first frame
        self.current_texture = 0
        self.textures = texture_list

    def update(self):
        # Update to the next frame of the animation. If we are at the end
        # of our frames, then delete this sprite.
        self.current_texture += 1
        if self.current_texture < len(self.textures):
            self.set_texture(self.current_texture)
        else:
            self.kill()

def create_explosion(texture_list, x, y):
    x = Explosion(texture_list)
    x.center_x = x
    x.center_y = y
    return x