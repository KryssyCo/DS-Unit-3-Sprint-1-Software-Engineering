'''
OOP Lecture Bruno
'''
from random import random

class Game:
    """ A general repesentation of a game"""
    def __init__(self, player1='Tina', player2='Raul'):
        self.round = 1
        self.player1 = player1
        self.player2 = player2
        
    def print_players(self):
        """Print the players of the game"""
        print('{} is playing {}'.format(self.player1, self.player2))

    def add_rounds(self):
        """Incrementing the number of rounds by 1"""
        self.round += 1

    def winner(self):
        return(self.player1 if random() > 0.5 else self.player2)  


class TicTacToe(Game):
    def __init__(self, player1='Joe', player2='Bill'):
        super().__init__(player1, player2)

    def print_players(self):
        """Print the players of the game"""
        print('{} is playing Tic- Tac-Toe with {}'.format(self.player1,
                                                           self.player2)) 
        
    
