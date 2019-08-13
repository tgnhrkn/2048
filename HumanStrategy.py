import curses

class HumanStrategy():

    input_map = {
        'w':'u',
        'd':'r',
        's':'d',
        'a':'l',
    }

    def __init__( self, win ):
        self.win = win
        self.win.leaveok( False )

    def move( self, board ):
        self.win.addstr( 0, 0, board.board_str() )
        self.win.refresh()
        while True:
            c = self.win.getch()
            if c == -1:
                continue

            if chr(c) in self.input_map :
                return self.input_map[chr(c)]
