class Dice_hand:

    def __init__(self):
        """Init the object"""
        self.__rolled = 0
        self.__history = []

    def add_rolled(self, value):
        """Adds points to current round"""
        self.__rolled += value

    def add_history(self, value):
        """Adds rolls to history"""
        self.__history.append(value)

    def get_history(self):
        """Returns history of rolls"""
        return self.__history

    def clear_history(self):
        """Clears history"""
        self.__history.clear()

    def clear_rolled(self):
        """Clears rolled from round"""
        self.__rolled = 0

    def get_rolled(self):
        """Returns rolled during current round"""
        return self.__rolled

    def print_hand(self):
        """Prints rolled this round"""
        print("Hand: ")
        print(self.__rolled)
