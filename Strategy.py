
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
    def move( self, board ):
       board.print_game()
       mv = input("Move: ")
       return mv
