from game.actor import Actor
from game.score import Score


class Player(Actor):
    """The entity controlled by the player.

    Hierarchy: Actor | Player

        Attributes:
        _score: The points scored by the player.
    """

    def __init__(self):
        super().__init__()
        self.score = Score()


