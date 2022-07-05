from game.artifact import Artifact


class Stone(Artifact):
    def __init__(self):
        """An individual gem.

        Hierarchy: Actor | Artifact | Stone

        Attributes:
            _points: THe point value of the stone.
        """
        super().__init__()
        self._points = -1

    def get_points(self):
        """Getter for _points.

        """

        return self._points
