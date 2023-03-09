import random


class Dice:

    def __init__(self):
        self.__value = 0
        self.output = ""

    def get_value(self):
        return self.__value

    def roll_dice(self):
        self.__lowerValue = 1
        self.__higherValue = 7
        self.__value = random.randrange(self.__lowerValue, self.__higherValue)

    def get_higher_value(self):
        return self.__higherValue
    
    def get_lower_value(self):
        return self.__lowerValue

    def set_value(self, newValue):
        self.__value = newValue
        print(self.__value)

    def print_face(self):
        if self.__value != 0:
            if self.__value == 1:
                self.output = """
                 ---------
                |         |
                |    *    |
                |         |
                 ---------
                """
            elif self.__value == 2:
                self.output = """
                 ---------
                |  *      |
                |         |
                |      *  |
                 ---------
                """
            elif self.__value == 3:
                self.output = """
                 ---------
                |  *      |
                |    *    |
                |      *  |
                 ---------
                """
            elif self.__value == 4:
                self.output = """
                 ---------
                |  *   *  |
                |         |
                |  *   *  |
                 ---------
                """
            elif self.__value == 5:
                self.output = """
                 ---------
                |  *   *  |
                |    *    |
                |  *   *  |
                 ---------
                """
            else:
                self.output = """
                 ---------
                |  *   *  |
                |  *   *  |
                |  *   *  |
                 ---------
                """
            print(self.output)
