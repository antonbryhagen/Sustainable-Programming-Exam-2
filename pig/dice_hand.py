class Dice_hand:

    def __init__(self):
        self.__rolled = 0
        self.__history = []

    def add_rolled(self, value):
        self.__rolled += value

    def add_history(self, value):
        self.__history.append(value)

    def get_history(self):
        return self.__history

    def clear_history(self):
        self.__history.clear()

    def clear_rolled(self):
        self.__rolled = 0

    def get_rolled(self):
        return self.__rolled

    def print_hand(self):
        print("Hand: ")
        print(self.__rolled)
