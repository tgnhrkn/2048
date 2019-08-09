import curses, time

class UpLeftStrategy():
  def __init__( self ):
    self.c_move = 'u'

  def move( self, board ):
    if(self.c_move == 'u'):
      self.c_move = 'l'
    else:
      self.c_move = 'u'
    return self.c_move

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
            return self.input_map[chr(c)]
