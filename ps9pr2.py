#
# ps9pr2.py (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

# write your class below.

class Player:
    """ a data type to represent a player of the Connect Four game
    """   
    
    def __init__(self, checker):
        """ constructs a new Player object"""
        assert(checker == 'X' or checker == 'O')
        
        self.checker = checker
        self.num_moves = 0
    
    def __repr__(self):
        """ returns a string representing a Player object """
        
        if self.checker == 'X':
            return 'Player X'
        
        else:
            return 'Player O'
    
    def opponent_checker(self):
        """ returns a one-character string representing the checker of the 
        Player object’s opponent
        """
        
        if self.checker == 'X':
            return 'O'
        
        else: 
            return 'X'

    def next_move(self, b):
        """ gets a next move for this player that is valid for the board b"""
        
        self.num_moves += 1
        
        while True:
            
            col = int(input('Enter a column: '))
            
            if b.can_add_to(col) == True:
                return col
            
            else:
                print('Try again!')
        