import random
import operator
import numpy as np
from Game import Standard2048Game
from Strategy import RandomStrategy

class MonteCarloStrategy:
    
    def __init__( self, background_runs=1 ):
        self.background_runs = background_runs

    def move( self, board ):
        return SerialMCRunner().run( runs=self.background_runs, board=board )[1]        
        

class SerialMCRunner():

    def run( self, runs, board ):
        
        run_stats = {
            'u' : [],
            'd' : [],
            'l' : [],
            'r' : [],
        }

        h, w = board.shape()
        game = Standard2048Game( RandomStrategy(), height=h, width=w, max_stuck=0 ) 

        for _ in range( runs ):
            brd_copy = board.get_copy()
            
            results = game.setup_and_play( board=brd_copy )
            
            run_stats[ results['movelist'][0] ].append( results['points'] )

        avgs = {
            'u' : 0.0,
            'd' : 0.0,
            'l' : 0.0,
            'r' : 0.0,
        }

        for fmove, xs in run_stats.items():
            if len( xs ):
                avgs[fmove] = np.average( np.array( xs ) )

        return avgs, max( avgs.items(), key=operator.itemgetter(1) )[0]
