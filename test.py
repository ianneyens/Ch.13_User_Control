import arcade
SW = 600
SH = 600


class Ball:
    def __init__(self, x, y, dx, dy, r, c):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.r = r
        self.c = c

    def draw_ball(self):
        arcade.draw_circle_filled(self.x, self.y, self.r, self.c)

    def update_ball(self):
        self.x += self.dx
        self.y += self.dy

        if self.x <= self.r:
            self.dx = 0
            self.x = self.r
        elif self.x >= SW - self.r:
            self.dx = 0
            self.x = SW - self.r
        elif self.y <= self.r:
            self.dy = 0
            self.y = self.r
        elif self.y >= SH - self.r:
            self.dy = 0
            self.y = SH - self.r


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.snd = arcade.load_sound("sounds/fighter_sound.ogg")
        self.set_mouse_visible(True)
        arcade.set_background_color(arcade.color.RED_DEVIL)
        self.ball = Ball(300, 300, 0, 0, 25, arcade.color.VIVID_SKY_BLUE)

    def on_draw(self):
        arcade.start_render()
        self.ball.draw_ball()

    def on_update(self, delta_time: float):
        self.ball.update_ball()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.ball.dx = -10
            arcade.play_sound(self.snd)
        elif key == arcade.key.RIGHT:
            self.ball.dx = 10
            arcade.play_sound(self.snd)
        elif key == arcade.key.UP:
            self.ball.dy = 10
            arcade.play_sound(self.snd)
        elif key == arcade.key.DOWN:
            self.ball.dy = -10
            arcade.play_sound(self.snd)

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.ball.dx = 0
            arcade.stop_sound(self.snd)
        elif key == arcade.key.RIGHT:
            self.ball.dx = 0
            arcade.stop_sound(self.snd)
        elif key == arcade.key.UP:
            self.ball.dy = 0
            arcade.stop_sound(self.snd)
        elif key == arcade.key.DOWN:
            self.ball.dy = 0
            arcade.stop_sound(self.snd)


"""            ***Mouse movement***
    def on_mouse_motion(self, x, y, dx, dy):
        self.ball.x = x
        self.ball.y = y

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            print("Left mouse button clicked at", x, y)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            print("Right mouse button clicked at", x, y)
"""


def main():
    window = Game(SW, SH, "Game")
    arcade.run()


if __name__ == '__main__':
    main()
