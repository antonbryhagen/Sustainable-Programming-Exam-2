class Intelligence:

    def play(self, difficulty, hand, game):
        if difficulty == 1:
            if hand.get_rolled() < 10:
                game.roll()
            else:
                game.hold()