import random
import operator
import numpy as np
from Game import Standard2048Game
from Strategy import RandomStrategy
import multiprocessing as mp

class MonteCarloStrategy:
    
    def __init__( self, background_runs=1, parallel=False, n_proc=1 ):
        self.background_runs = background_runs
        self.parallel = parallel
        self.n_proc = n_proc

    def move( self, board ):
        if self.parallel: 
            mv = ParallelMCRunner( self.n_proc ).run( runs=self.background_runs, board=board )[1]
            return mv
        else:
            return SerialMCRunner().run( runs=self.background_runs, board=board )[1]

class MonteCarloVizStrategy( MonteCarloStrategy ):
    
    def __init__( self, win, background_runs=1, parallel=False, n_proc=1 ):
        super().__init__( background_runs, parallel, n_proc )
        self.win = win

    def move( self, board ): 
        self.win.addstr( 0, 0, board.board_str() )
        self.win.refresh()
        return super().move( board )

class ParallelMCRunner():
    
    def __init__( self, n_proc ):
        self.n_proc = n_proc

    def run( self, runs, board ):
        def work( runs, board, q ):
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
           
            q.put( run_stats )
        
        runs_q = mp.Queue()

        stats = {
            'u' : [],
            'd' : [],
            'l' : [],
            'r' : [],
        }

        runs_per = int( runs / self.n_proc )
        n_extra = int( runs % self.n_proc )
        xs = [ runs_per for _ in range( self.n_proc ) ]
        for i in range( n_extra ):
            xs[i] += 1
        

        procs = [ mp.Process( target=work, args=(xs[i], board, runs_q,) ) for i in range(self.n_proc) ]
        list( map( lambda x: x.start(), procs ) )
        list( map( lambda x: x.join(), procs ) )

        while not runs_q.empty():
            s = runs_q.get()
            for fmove, lst in s.items():
                stats[fmove] += lst

        avgs = {
            'u' : 0.0,
            'd' : 0.0,
            'l' : 0.0,
            'r' : 0.0,
        }

        for fmove, xs in stats.items():
            if len( xs ):
                avgs[fmove] = np.average( np.array( xs ) )

        return avgs, max( avgs.items(), key=operator.itemgetter(1) )[0]

        



        


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
