from game.artifact import Artifact


class Score:
    """The score of the game.

    Hierarchy: Score

    Attributes:
        _score: Value of the game score.
    """

    def __init__(self):
        super().__init__()
        self._score = 0

    def get_score(self):
        """Getter for _score.

        """

        return self._score

    def add_score(self, value):
        """Modify score based on a value.

        Params:
            value: Amount to modify score by.

        """

        self._score += value
