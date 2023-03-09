class Intelligence:

    def play(self, difficulty, hand, opponent_score, our_score):
        """Decides computers next move"""
        self.difference = 0
        if difficulty == "1":
            if hand.get_rolled() < 20:
                return "roll"
            else:
                return "hold"
        elif difficulty == "2":
            if hand.get_rolled() < 25:
                return "roll"
            else:
                return "hold"
        elif difficulty == "3":
            if opponent_score > our_score:
                self.difference = (opponent_score - our_score) / 8
            if our_score > opponent_score:
                self.difference = (our_score - opponent_score) / 8
            if hand.get_rolled() >= 71 or opponent_score >= 71:
                return "roll"
            elif hand.get_rolled() > 21 + self.difference:
                return "hold"
            else:
                return "roll"
