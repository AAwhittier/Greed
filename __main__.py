import os
import random

from services.keyboard_service import KeyboardService
from services.video_service import VideoService

from game.cast import Cast
from game.actor import Actor
from game.gem import Gem
from game.stone import Stone
from game.player import Player

from utility.color import Color
from utility.director import Director
from utility.point import Point

FRAME_RATE = 15
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed"
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
GREEN = Color(0, 255, 0)
DEFAULT_ARTIFACTS = 40

def main():
    """
    Sets up the initial game needs and structure before passing control to the Director.

    """

    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)

    entities = Cast()

    x = int(MAX_X / 2)
    y = int(MAX_Y - 1)
    position = Point(x, y)
    player = Player()
    player.set_text("#")
    player.set_font_size(FONT_SIZE)
    player.set_color(WHITE)
    position = position.scale(CELL_SIZE)
    player.set_position(position)
    entities.add_actor("Player", player)

    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    entities.add_actor("Banners", banner)

    for n in range(DEFAULT_ARTIFACTS):

        selector = random.randint(0, 99)

        # Select which should spawn, a gem or a rock.
        if selector % 2 == 0:
            artifact = Gem()
            artifact.set_font_size(FONT_SIZE)
            artifact.set_color(GREEN)
            x = random.randint(1, COLS - 1)
            y = random.randint(1, ROWS - 1)
            position = Point(x, y)
            position = position.scale(CELL_SIZE)
            artifact.set_position(position)
            artifact.set_text("$")
        else:
            artifact = Stone()
            artifact.set_font_size(FONT_SIZE)
            artifact.set_color(RED)
            x = random.randint(1, COLS - 1)
            y = random.randint(1, ROWS - 1)
            position = Point(x, y)
            position = position.scale(CELL_SIZE)
            artifact.set_position(position)
            artifact.set_text("@")

        entities.add_actor("Artifacts", artifact)

    director = Director(keyboard_service, video_service)
    director.start_game(entities)


if __name__ == "__main__":
    main()
