"""
Sign your name:Ian
 
Update the code in this chapter to do the following:
Open a 500px by 500px window.
Change the Ball class to a Box class.
Instantiate two 30px by 30px boxes. One red and one blue.
Make the blue box have a speed of 240 pixels/second
Make the red box have a speed of 180 pixels/second
Control the blue box with the arrow keys.
Control the red box with the WASD keys.
Do not let the boxes go off of the screen.
Incorporate different sounds when either box hits the edge of the screen.
Have two people play this TAG game at the same time.
The red box is always "it" and needs to try to catch the blue box.
When you're done demonstrate to your instructor!
"""
import arcade
SW = 500
SH = 500
rs = 3
bs = 4


class Box:
    def __init__(self, x, y, dx, dy, s, c):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.s = s
        self.c = c
        if self.c == arcade.color.RED:
            self.snd = arcade.load_sound("laser.mp3")
        elif self.c == arcade.color.BLUE:
            self.snd = arcade.load_sound("explosion.mp3")

    def draw_box(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.s, self.s, self.c)

    def update_box(self):
        self.x += self.dx
        self.y += self.dy

        if self.x <= self.s / 2:
            self.dx = 0
            self.x = self.s / 2
            arcade.play_sound(self.snd)
        elif self.x >= SW - self.s / 2:
            self.dx = 0
            self.x = SW - self.s / 2
            arcade.play_sound(self.snd)
        elif self.y <= self.s / 2:
            self.dy = 0
            self.y = self.s / 2
            arcade.play_sound(self.snd)
        elif self.y >= SH - self.s / 2:
            self.dy = 0
            self.y = SH - self.s / 2
            arcade.play_sound(self.snd)


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_mouse_visible(True)
        arcade.set_background_color(arcade.color.WHITE)
        self.red_box = Box(25, 250, 0, 0, 30, arcade.color.RED)
        self.blue_box = Box(475, 250, 0, 0, 30, arcade.color.BLUE)

    def on_draw(self):
        arcade.start_render()
        self.red_box.draw_box()
        self.blue_box.draw_box()

    def on_update(self, delta_time: float):
        self.red_box.update_box()
        self.blue_box.update_box()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.blue_box.dx = -bs
        elif key == arcade.key.RIGHT:
            self.blue_box.dx = bs
        elif key == arcade.key.UP:
            self.blue_box.dy = bs
        elif key == arcade.key.DOWN:
            self.blue_box.dy = -bs
        elif key == arcade.key.W:
            self.red_box.dy = rs
        elif key == arcade.key.A:
            self.red_box.dx = -rs
        elif key == arcade.key.S:
            self.red_box.dy = -rs
        elif key == arcade.key.D:
            self.red_box.dx = rs

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.blue_box.dx = 0
        elif key == arcade.key.RIGHT:
            self.blue_box.dx = 0
        elif key == arcade.key.UP:
            self.blue_box.dy = 0
        elif key == arcade.key.DOWN:
            self.blue_box.dy = 0
        elif key == arcade.key.W:
            self.red_box.dy = 0
        elif key == arcade.key.A:
            self.red_box.dx = 0
        elif key == arcade.key.S:
            self.red_box.dy = 0
        elif key == arcade.key.D:
            self.red_box.dx = 0


def main():
    window = Game(SW, SH, "Game")
    arcade.run()


if __name__ == '__main__':
    main()
