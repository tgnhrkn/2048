from Board import Board_2048
import numpy as np

class Standard2048Game:

    def __init__( self, strategy, width=4, height=4, max_stuck=3 ):
        self.strategy = strategy
        self.width = width
        self.height = height
        self.max_stuck = max_stuck
        self.board = None
        self.points = None
    
    def start( self ):
        self.board = Board_2048( width=self.width, height=self.height )
        self.board.place_random_tile()
        self.board.place_random_tile()
        self.points = 0
        self.turns = 0

    def finish( self ):
        if not self.board:
            return ( self.points, "Game not started" )

        stuck_moves = 0
        while not self.board.stuck() and not stuck_moves > self.max_stuck:
            ( p, m ) = self.board.slide( self.strategy.move( self.board ) )
            self.points = self.points + p
            if m:
                self.board.place_random_tile()
                self.turns = self.turns + 1
            elif self.max_stuck > 0:
                stuck_moves = stuck_moves + 1
        
        finstr = ""
        if ( stuck_moves > self.max_stuck ):
            finstr = "Strategy got stuck\n"
        else:
            finstr = "Stuck board\n"

        return self.points, self.turns, finstr + "Final Board: (%d points)\n" % self.points + self.board.board_str()

    def play( self ):
        self.start()
        return self.finish()


class GameTracker:
    
    def __init__( self, game, rounds=1, options={} ):
        self.game = game
        self.rounds = rounds
        self.options = options

        self.gameinfo = np.empty( ( 0, 2 ), int )

    def run( self ):
        
        for _ in range( self.rounds ):
            points, turns, _ = self.game.play()
            self.gameinfo = np.append( self.gameinfo, [[points, turns]], axis=0 )

    def averages( self ):
        sums = np.sum(self.gameinfo, axis=0)
        avg_dict = {
            'points_avg': sums[0] / self.rounds,
            'turns_avg': sums[1] / self.rounds,
        }
        return avg_dict
