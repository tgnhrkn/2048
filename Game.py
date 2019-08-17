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
        self.movelist = None
    
    def setup( self, board=None ):
        if board is None:
            self.board = Board_2048( width=self.width, height=self.height )
            self.board.place_random_tile()
            self.board.place_random_tile()
        elif board.shape() == ( self.height, self.width ):
            self.board = board
        else:
            raise Exception( "setup shape does not match init shape" )

        self.points = 0
        self.turns = 0
        self.movelist = []

    def play_to_end( self ):
        if not self.board:
            raise Exception( "Game not setup" )

        stuck_moves = 0
        while not self.board.stuck() and not stuck_moves > self.max_stuck:
            move = self.strategy.move( self.board )
            ( p, m ) = self.board.slide( move )
            self.points = self.points + p
            if m:
                self.board.place_random_tile()
                self.turns = self.turns + 1
                self.movelist.append( move )
            elif self.max_stuck > 0:
                stuck_moves = stuck_moves + 1
        
        finstr = ""
        if ( stuck_moves > self.max_stuck ):
            finstr = "Strategy got stuck\n"
        else:
            finstr = "Stuck board\n"

        return {
            'points': self.points, 
            'total': self.board.total(),
            'turns': self.turns,
            'movelist': self.movelist,
            'endstr': finstr + "Final Board: (%d points)\n" % self.points + self.board.board_str(),
            'max': self.board.max(),
        }

    def setup_and_play( self, board=None ):
        self.setup( board=board )
        return self.play_to_end()


class GameTracker:
    
    def __init__( self, game, rounds=1, options={} ):
        self.game = game
        self.rounds = rounds
        self.options = options
        self.gameinfo = np.empty( ( 0, 2 ), int )

    def run( self ):
        
        for _ in range( self.rounds ):
            results = self.game.setup_and_play()
            self.gameinfo = np.append( self.gameinfo, [[results['points'], results['turns']]], axis=0 )

    def averages( self ):
        sums = np.sum(self.gameinfo, axis=0)
        avg_dict = {
            'points_avg': sums[0] / self.rounds,
            'turns_avg': sums[1] / self.rounds,
        }
        return avg_dict
