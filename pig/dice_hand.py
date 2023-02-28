class Dice_hand:

    def __init__(self):
        self.__rolled = []

    def add_rolled(self, new_dice):
        self.__rolled.append(new_dice)

    def clear_rolled(self):
        self.__rolled.clear()

    def get_rolled(self):
        return self.__rolled

    def print_hand(self):
        print("Hand: ")
        for element in self.__rolled:
            print(element.get_value())

    def get_score(self):
        __score = 0
        for element in self.__rolled:
            __score += element.get_value()
        return __score
