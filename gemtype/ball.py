import arcade

class Ball:
    def __init__(self, max_width, max_height, position_x, position_y, change_x, change_y, radius, color):

        # Take the parameters of the init function above, and create instance variables out of them.
        self.max_width = max_width
        self.max_height = max_height
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

    def update(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > self.max_width - self.radius:
            self.position_x = self.max_width - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > self.max_height - self.radius:
            self.position_y = self.max_height - self.radius