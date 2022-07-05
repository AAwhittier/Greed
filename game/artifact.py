from game.actor import Actor
from utility.point import Point
import random

class Artifact(Actor):
    """
    An item of cultural or historical interest.

    The responsibility of an Artifact is to provide a message about itself.

    Attributes:
        _message (string): A short description about the artifact.
    """

    def __init__(self):
        super().__init__()
        self._max_x = 900
        self._cell_size = 15

    def fall(self):
        """Simulates a falling artifact.

        Sets position based on the characters position on screen and bring sit back to the top when it
        has reached the bottom.
        """

        if self.get_position().get_y() < 600:
            self.set_position(Point(self.get_position().get_x(), self.get_position().get_y() + 5))
        else:
            self.respawn()

    def respawn(self):
        """Brings the artifact back to a new starting position.

        Sets position based on the top of screen.
        """

        position = Point(random.randint(0, self._max_x / self._cell_size), 0)
        position = position.scale(15)
        self.set_position(position)



