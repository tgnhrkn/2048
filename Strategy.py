class AllFourStrategy():
    
    moves = ['u', 'r', 'l', 'd']
    
    def __init__( self ):
        self.i = 0

    def move( self, board ):
        mv = self.moves[self.i]
        self.i = ( self.i + 1 ) % 4
        return mv


class UpLeftStrategy():
  def __init__( self ):
    self.c_move = 'u'

  def move( self, board ):
    if(self.c_move == 'u'):
      self.c_move = 'l'
    else:
      self.c_move = 'u'
    return self.c_move
