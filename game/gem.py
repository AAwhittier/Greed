from game.artifact import Artifact


class Gem(Artifact):
    """An individual gem.

    Hierarchy: Actor | Artifact | Gem

        Attributes:
        _points: THe point value of the gem.
    """
    def __init__(self):
        super().__init__()
        self._points = 1

    def get_points(self):
        """Getter for _points.

        """

        return self._points
