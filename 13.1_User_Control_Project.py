"""
USER CONTROL PROJECT
-----------------
Your choice!!! Have fun and be creative.
Create a background and perhaps animate some objects.
Pick a user control method and navigate an object around your screen.
Make your object more interesting than a ball.
Create your object with a new class.
Perhaps move your object through a maze or move the object to avoid other moving objects.
Incorporate some sound.
Type the directions to this project below:

DIRECTIONS:
----------
Please type directions for this game here.
"""
import arcade
import random

SW = 800
SH = 600
pscale = .1
bscale = .1
cscale = .1
SPD = 5
CSPD = 2.5
BSPD = 5
COINS = 50
BOMBS = 30


class Player(arcade.Sprite):
    def __init__(self):
        super().__init__("ship.png", pscale)

    def update(self):
        self.center_x += self.change_x

        if self.right > SW:
            self.right = SW
        elif self.left > SW:
            self.left = 0


class Bomb(arcade.Sprite):
    def __init__(self):
        super().__init__("bomb.png", bscale)
        self.w = int(self.width)
        self.h = int(self.height)

    def update(self):
        self.center_y -= BSPD
        if self.top < 0:
            self.center_x = random.randint(self.w, SW - self.w)
            self.center_y = random.randint(SH + self.h, SH * 2)


class Coin(arcade.Sprite):
    def __init__(self):
        super().__init__("coin.png", cscale)
        self.w = int(self.width)
        self.h = int(self.height)

    def update(self):
        self.center_y -= CSPD
        if self.top < 0:
            self.center_x = random.randint(self.w, SW - self.w)
            self.center_y = random.randint(SH + self.h, SH * 2)


class MyGame(arcade.Window):

    def __init__(self, SW, SH, title):
        super().__init__(SW, SH, title)
        self.score = 0
        self.set_mouse_visible(False)
        self.current_state = 0
        self.gameover = True

    def reset(self):
        if self.current_state == 1:
            self.background = arcade.load_texture("background.jpg")
            self.coin_count = 50
            self.bomb_count = 50

        self.player_list = arcade.SpriteList()
        self.bomb_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        self.player = Player()
        self.player.center_x = SW / 2
        self.player.center_y = SH / 20
        self.player_list.append(self.player)

        for i in range(COINS):
            coin = Coin()
            coin.center_x = random.randrange(10, 790)
            coin.center_y = random.randrange(SH + 10, SH * 2)
            self.coin_list.append(coin)

        for i in range(BOMBS):
            bomb = Bomb()
            bomb.center_x = int(random.randrange(10, 790))
            bomb.center_y = int(random.randrange(SH + 10, SH * 2))
            self.bomb_list.append(bomb)

    def on_draw(self):
        arcade.start_render()

        if self.current_state == 0:
            arcade.draw_rectangle_filled(SW / 2, SH / 2, SW, SH, arcade.color.BLACK)
            arcade.draw_text("Use arrow keys to move, collect as many coins as possible and avoid the bombs",
                             SW / 2, SH / 2 - 30, arcade.color.GHOST_WHITE, 14, align="center", anchor_x="center")
        elif not self.gameover:
            arcade.draw_texture_rectangle(SW / 2, SH / 2, SW, SH, arcade.load_texture("background.jpg"))
            self.player_list.draw()
            self.bomb_list.draw()
            self.coin_list.draw()

            the_score = f"Score: {self.score}"
            arcade.draw_text(the_score, SW - 90, SH - 35, arcade.color.BLACK, 14)

        else:
            output = f"Score: {self.score}"
            arcade.draw_rectangle_filled(SW / 2, SH / 2, SW, SH, arcade.color.BLACK)
            arcade.draw_text("Game Over! Press SPACE to play again", SW / 2, SH / 2 - 30,
                             arcade.color.GHOST_WHITE, 14, align="center", anchor_x="center")
            arcade.draw_text(output, SW / 2, SH / 2 - 50, arcade.color.GHOST_WHITE, 14, align="center",
                             anchor_x="center")

    def on_update(self, dt):
        if 0 < self.current_state < 2:
            self.gameover = False
        else:
            self.gameover = True

        if not self.gameover:
            self.player_list.update()
            self.bomb_list.update()
            self.coin_list.update()

            if not self.coin_list:
                self.gameover = True

            coin_hit = arcade.check_for_collision_with_list(self.player, self.coin_list)
            if len(coin_hit) > 0 and not self.gameover:

                for coin in coin_hit:
                    coin.kill()
                    self.score += 1

                if len(self.coin_list) == 0:
                    self.current_state += 1
                    self.reset()

            plane_bombed = arcade.check_for_collision_with_list(self.player, self.bomb_list)
            if len(plane_bombed) > 0 and not self.gameover:
                self.player.kill()
                plane_bombed[0].kill()
                self.current_state = 2

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP and not self.gameover:
            self.player.change_y = SPD
        elif key == arcade.key.DOWN and not self.gameover:
            self.player.change_y = -SPD
        elif key == arcade.key.RIGHT and not self.gameover:
            self.player.change_x = SPD
        elif key == arcade.key.LEFT and not self.gameover:
            self.player.change_x = -SPD
        elif key == arcade.key.SPACE:
            self.reset()
            self.current_state = 1
            self.score = 0

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.change_y = 0
        elif key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.player.change_x = 0


def main():
    window = MyGame(SW, SH, "BB8 Explosions")
    arcade.run()


# ------Run Main Function-----


if __name__ == "__main__":
    main()
