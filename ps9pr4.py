#
# ps9pr4.py (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four  
#

import random  
from ps9pr3 import *

class AIPlayer(Player):
    
    def __init__(self, checker, tiebreak, lookahead):
        """ constructs a new AIPlayer object
        """
        
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        
    def __repr__(self):
        """ returns a string representing an AIPlayer object 
        """
        
        s = super().__repr__()
        mo = str(self.lookahead)
        move = str(self.tiebreak)
        s += ' (' + move +  ", "  + mo + ')'
        return s
    
    def max_score_column(self, scores): 
        """ takes a list of scores containing a score for each column of the board, 
        and that returns the index of the column with the maximum score
        """
        
        score = max(scores)
        
        lists = []
        
        for i in range(len(scores)):
            
            if scores[i] == score:
                lists += [i]

    
        if self.tiebreak == 'LEFT':
            move = lists[0]
            return move
        
        elif self.tiebreak == 'RIGHT':
            move = lists[-1]
            return move
        
        else:
            move = random.choice(lists)
            return move
    
    def scores_for(self, b):
        """ returns a list of scores - one for each col in board b 
        """
        
        scores = [50] * b.width
        
        for col in range(b.width):
  
            if b.can_add_to(col) == False:
                scores[col] = -1
            
            elif b.is_win_for(self.checker) == True:
                scores[col] = 100
                
            elif b.is_win_for(self.opponent_checker()) == True:
                scores[col] = 0
            
            elif self.lookahead == 0:
                scores[col] = 50
            
            else:
                b.add_checker(self.checker, col)
                
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                
                opp_scores = opponent.scores_for(b)
                
                if max(opp_scores) == 100:
                    win = 100 - max(opp_scores)
                    scores[col] = win
                    
                elif max(opp_scores) == 50:
                    win = 100 - max(opp_scores)
                    scores[col] = win
                
                elif max(opp_scores) == 0:
                    win = 100 - max(opp_scores)
                    scores[col] = win
                
                b.remove_checker(col)
                
        return scores
    
    def next_move(self, b): 
        """ return the called AIPlayer‘s judgment of its best possible move
        """
        
        self.num_moves += 1
            
        move = self.max_score_column(self.scores_for(b))
        return move
        
        
        