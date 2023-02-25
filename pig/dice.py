import random

class Dice:

    def __init__(self):
        self.__value = 0

    def get_value(self):
        return self.__value

    def roll_dice(self):
        self.__value = random.randrange(1, 7)

    def set_value(self, newValue):
        self.__value = newValue
        print(self.__value)

    def print_face(self):
        if self.__value != 0:
            if self.__value == 1:
                print("""
                 ---------
                |         |
                |    *    |
                |         |
                 ---------
                """)
            elif self.__value == 2:
                print("""
                 ---------
                |  *      |
                |         |
                |      *  |
                 ---------
                """)
            elif self.__value == 3:
                print("""
                 ---------
                |  *      |
                |    *    |
                |      *  |
                 ---------
                """)
            elif self.__value == 4:
                print("""
                 ---------
                |  *   *  |
                |         |
                |  *   *  |
                 ---------
                """)
            elif self.__value == 5:
                print("""
                 ---------
                |  *   *  |
                |    *    |
                |  *   *  |
                 ---------
                """)
            else:
                print("""
                 ---------
                |  *   *  |
                |  *   *  |
                |  *   *  |
                 ---------
                """)

    def main():
        pass

    if __name__ == '__main__':
        main()