"""Handle computers moves."""


class Intelligence:
    """Intelligence class."""

    def __init__(self):
        """Init the object."""
        self.difference = 0

    def play(self, difficulty, hand, opponent_score, our_score):
        """Decide computers next move."""
        choice = ""
        if difficulty == "1":
            choice = self.play_dif_1(hand)
        elif difficulty == "2":
            choice = self.play_dif_2(hand)
        elif difficulty == "3":
            choice = self.play_dif_3(hand, opponent_score, our_score)
        return choice

    def play_dif_1(self, hand):
        """Decide action with difficulty 1."""
        if hand.get_rolled() < 20:
            return "roll"
        return "hold"

    def play_dif_2(self, hand):
        """Decide action with difficulty 2."""
        if hand.get_rolled() < 25:
            return "roll"
        return "hold"

    def play_dif_3(self, hand, opponent_score, our_score):
        """Decide action with difficulty 3."""
        if opponent_score >= our_score:
            self.difference = (opponent_score - our_score) / 8
        if our_score >= opponent_score:
            self.difference = (our_score - opponent_score) / 8
        if hand.get_rolled() >= 71 or opponent_score >= 71:
            return "roll"
        if hand.get_rolled() > 21 + self.difference:
            return "hold"
        return "roll"
