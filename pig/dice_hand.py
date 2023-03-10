"""Handles current hand."""


class Dice_hand:
    """Dice_hand class."""

    def __init__(self):
        """Init the object."""
        self.__rolled = 0
        self.__history = []

    def add_rolled(self, value):
        """Add points to current round."""
        self.__rolled += value

    def add_history(self, value):
        """Add rolls to history."""
        self.__history.append(value)

    def get_history(self):
        """Return history of rolls."""
        return self.__history

    def clear_history(self):
        """Clear history."""
        self.__history.clear()

    def clear_rolled(self):
        """Clear rolled from round."""
        self.__rolled = 0

    def get_rolled(self):
        """Return rolled during current round."""
        return self.__rolled

    def print_hand(self):
        """Print rolled this round."""
        print("Hand: ")
        print(self.__rolled)
