class Dice:

    def __init__(self):
        pass

    __value = 0

    def getValue(self):
        return self.__value

    def setValue(self, newValue):
        self.__value = newValue
        print(self.__value)

    def printFace(self):
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
