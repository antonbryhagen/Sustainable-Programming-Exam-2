class Player:
    """Player class."""

    def __init__(self, name):
        """Init the object."""
        self._name = name
        self._score = 0  # Start player score at zero
        self._current_turn_score = 0  # Set current turn score to zero

    def get_name(self):
        """Get player name."""
        return self._name

    def set_name(self, name):
        """Set player name."""
        self._name = name

    def get_score(self):
        """Get player score."""
        return self._score

    def set_score(self, score):
        """Set player score."""
        self._score = score
