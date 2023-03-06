class Dice_hand:

    def __init__(self):
        self.__rolled = 0

    def add_rolled(self, value):
        self.__rolled += value

    def clear_rolled(self):
        self.__rolled = 0

    def get_rolled(self):
        return self.__rolled

    def print_hand(self):
        print("Hand: ")
        print(self.__rolled)

    def get_score(self):
        return self.__rolled