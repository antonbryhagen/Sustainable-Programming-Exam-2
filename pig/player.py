class Player:
    def __init__(self, name):
        self._name = name
        self._score = 0 # Start player score at zero
        self._current_turn_score = 0 # Set current turn score to zero

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name

    def get_score(self):
        return self._score

    def set_score(self, score):
        self._score = score
    
    def get_current_turn_score(self):
        return self._current_turn_score

    def set_current_turn_score(self, turn_score):
        self._current_turn_score = turn_score
    
