from Board import Board_2048

class Standard2048Game:

    def __init__( self, strategy ):
        self.strategy = strategy
        self.board = None
        self.points = None
    
    def start( self ):
        self.board = Board_2048( 4 )
        self.board.place_random_tile()
        self.board.place_random_tile()
        self.points = 0

    def finish( self ):
        if not self.board:
            print( "Game not started" )
            return

        stuck_moves = 0
        while( not self.board.stuck() and not stuck_moves > 3):
            ( p, m ) = self.board.slide( self.strategy.move( self.board ) )
            self.points = self.points + p
            if m:
                self.board.place_random_tile()
            else:
                stuck_moves = stuck_moves + 1

        if ( stuck_moves > 3 ):
            print( "Strategy got stuck" )
        else:
            print( "Stuck board" )

        print( "Final Board: (%d points)" % self.points )
        self.board.print_game()

    def play( self ):
        self.start()
        self.finish()
        
