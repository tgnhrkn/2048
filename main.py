#!/usr/bin/python3
import numpy as np
import random

def board_copy( board ):
  return [row[:] for row in board]

def get_init_board():
  arr = [[],[],[],[]]
  for r in arr:
    for i in range(4):
      r.append(None)

  arr = place_new_tile( arr )
  arr = place_new_tile( arr )
  return arr

def place_new_tile( board ):
  copied = board_copy( board )
  opts = list(zip(*np.where(np.array(copied) == None)))
  if(len(opts) != 0):
    idx = random.sample(opts, 1)[0]
    copied[idx[0]][idx[1]] = 2
  return copied

def rot_right( arr ):
  list_of_tuples = zip(*arr[::-1])
  return [list(elem) for elem in list_of_tuples]

def print_board( board ):
  def print_row( row ):
    def p_e( e ):
      if e is None:
        return 0
      else:
        return e
      
    print( "%d %d %d %d" % (p_e(row[0]), p_e(row[1]), p_e(row[2]), p_e(row[3])))
  print("~~~~~~~~~~~~~~~~~")
  print_row(board[0])
  for r in board[1:4]:
    print()
    print_row(r)
  print("~~~~~~~~~~~~~~~~~")

def compress( arr ):
  a = []
  c = 0
  for i in arr:
    if i is not None:
      a.append(i)
    else:
      c = c + 1
  
  for i in range(c):
    a.append(None)
  
  for i in range(len(a) - 1):
    if a[i] is not None:
      if a[i] == a[i+1]:
        a[i] = a[i] * 2
        a[i + 1] = None
  
  a2 = []
  c = 0
  for i in a:
    if i is not None:
      a2.append(i)
    else:
      c = c + 1
  
  for i in range(c):
    a2.append(None)

  moved = a2 != arr
  return (a2, moved)

def compress_board_h( brd ):
  new_brd = [[], [], [], []]
  moved = False
  for i in range(len(brd)):
    res = compress( brd[i] )
    new_brd[i] = res[0]
    moved = moved or res[1]
  return (new_brd, moved)

def compress_board( brd, rots ):
  rots = rots % 4
  board = brd
  for i in range(rots):
    board = rot_right(board)
  (board, moved) = compress_board_h(board)
  for i in range(4 - rots):
    board = rot_right(board)
  return (board, moved)

def board_stuck( brd ):
  moved = False
  for i in range(4):
    _, m = compress_board(brd, i)
    moved = moved or m
  return not moved

class UpLeftStrategy():
  def __init__( self ):
    self.c_move = 'u'

  def move( self, board ):
    if(self.c_move == 'u'):
      self.c_move = 'l'
    else:
      self.c_move = 'u'
    return self.c_move

move_rot_map = {
  "l": 0,
  "r": 2,
  "d": 1,
  "u": 3,
}

def play( strategy ):
  board = get_init_board()
  stuck_count = 0
  while( not board_stuck( board ) and stuck_count < 3):
    print_board( board )
    move = strategy.move( board )
    ( brd, moved ) = compress_board( board, move_rot_map[move] )
    print("Move: %s, moved: %d" % (move, moved))
    board = brd
    if( not moved ):
      stuck_count = stuck_count + 1
    else:
      stuck_count = 0
      board = place_new_tile( board )

  if( stuck_count ):
    print("Stuck")
  else:
    print("Lost")
  return board

final = play( UpLeftStrategy() )
print_board( final )
#strat = BadStrategy()
#print(strat.move( None ))

