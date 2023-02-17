from dice import Dice


class Dice_hand:

    def __init__(self):
        self.__rolled = []
    
    def add_rolled(self, new_dice):
        self.__rolled.append(new_dice)
    
    def clear_rolled(self):
        self.__rolled.clear()

    def print_hand(self):
        for element in self.__rolled:
            print(Dice.get_value(element))  # type: ignore
