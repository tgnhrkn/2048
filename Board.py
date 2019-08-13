import numpy as np
import random

class Board_2048:
    
    def __init__( self, width=4, height=4 ):
        self.width = width
        self.height = height
        self.board = self.get_init_board()
        
    def board_str( self ):
        def get_lines():
            cap_str = "+"
            fill_str = "|"
            for _ in range(self.width):
                cap_str = cap_str + "-----+"
                fill_str = fill_str + "     |"
            return (cap_str + "\n", fill_str + "\n")

        (cap_line, fill_line) = get_lines()

        def row_str( row ):
            def e_str( e ):
                return  "" if e is None else str(e)

            ret = "|"
            for e in row:
                ret = ret + e_str(e).center( 5, ' ' ) + "|"
            return ret + "\n"

        brd = cap_line
        for row in self.board:
            brd = brd + fill_line + row_str( row ) + fill_line + cap_line
        return brd
        

    def print_game( self ):
        print( self.board_str() )

    def get_init_board( self ):
      arr = [[None for _ in range( self.width ) ] for _ in range( self.height ) ]
      return np.array(arr)

    def place_random_tile( self, val=2 ):
      opts = list(zip(*np.where(self.board == None)))
      if(len(opts) != 0):
        idx = random.sample(opts, 1)[0]
        self.board[idx[0]][idx[1]] = val

    def try_slide( self, direction ):
        temp_board = np.copy( self.board )
        res = self.slide( direction )
        del self.board
        self.board = temp_board
        return res

    def stuck( self ):
        moved = False
        for d in [ 'u', 'd', 'l', 'r' ]:
            _, m = self.try_slide( d )
            moved = moved or m
        return not moved

    def slide( self, direction ):

        def in_place_compress_left( arr ):
            cur_i = 0
            move_to = 0
            cur_val = None
            cur_val_orig_idx = None
            moved = False
            points = 0
            while cur_i < len( arr ):
                if cur_val is None and arr[cur_i] is not None:
                    cur_val = arr[cur_i]
                    cur_val_orig_idx = cur_i
                elif cur_val is not None and cur_val == arr[cur_i]:
                    arr[move_to] = cur_val * 2
                    points = points + cur_val * 2
                    moved = True
                    cur_val = None
                    move_to = move_to + 1
                elif arr[cur_i] is not None and cur_val != arr[cur_i]:
                    arr[move_to] = cur_val
                    if move_to != cur_val_orig_idx:
                        moved = True
                    cur_val = arr[cur_i]
                    cur_val_orig_idx = cur_i
                    move_to = move_to + 1
                cur_i = cur_i + 1
            arr[move_to] = cur_val
            if cur_val_orig_idx is not None and move_to != cur_val_orig_idx:
                moved = True
            move_to = move_to + 1
            while move_to < len( arr ):
                arr[move_to] = None
                move_to = move_to + 1

            return ( points, moved )

        def rc_get( val, direc ):
            if direc == 'u':
                return self.board[:,val]
            if direc == 'd':
                return self.board[::-1,val]
            if direc == 'l':
                return self.board[val]
            if direc == 'r':
                return self.board[val][::-1]
        
        points = 0
        moved = False
        for i in range( self.height if direction in [ 'l', 'r' ] else self.width ):
            ( p, m ) = in_place_compress_left( rc_get( i, direction ) )
            points = points + p
            moved = moved or m
        return ( points, moved )
