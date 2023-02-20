from player import Player
import pickle

class Highscore:
    def __init__(self):
        pass

    def get_highscores(self):
        #create dictionary if first time running game on new system
        highscores = dict()
        with open('highscores.bin', 'rb') as highscores_file:
            try:
                highscores = pickle.load(highscores_file)
            except EOFError:    #if no highscores (empty file), use empty dictionary
                pass
        return highscores

        
        #return table with scores from file
    
    def update_highscore(self, player: Player):
        highscores = self.get_highscores()
        
        if player in highscores:
            highscores[player] = [highscores[player]] #get stats and update wins and games played
        else:
            highscores[player] = [1] #add new player and games played
            
    #check for name in file, if name is there, update highscore
    #if name is not there, add it

    #Add new highscore
    #Read highscores
    #Store in table with Player obj and high score value
    
    #get as string / list method