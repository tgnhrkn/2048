#!/usr/bin/python3

from Board import Board_2048

brd = Board_2048( 4 )
brd.print()
for i in range(5):
    brd.place_random_tile()
brd.print()
p, m = brd.slide( 'd' )
brd.print()
print( p )
print( str(m) )

brd.print_game()
