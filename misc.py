#!/usr/bin/python3
import numpy as np

"""
arr = np.reshape( np.linspace(0,15,16), (4, 4) )
print( arr )

def get( val, direc, arr ):
    if direc == 'u':
        return arr[:,val]
    if direc == 'd':
        return arr[::-1,val]
    if direc == 'l':
        return arr[val]
    if direc == 'r':
        return arr[val][::-1]


print( get( 0, 'u', arr ) )
print( get( 0, 'd', arr ) )
print( get( 0, 'l', arr ) )
print( get( 0, 'r', arr ) )
print( get( 1, 'u', arr ) )
print( get( 1, 'd', arr ) )
print( get( 1, 'l', arr ) )
print( get( 1, 'r', arr ) )

print( arr )
r = get( 0, 'r', arr )
r[0] = 100.0
print( arr )
"""

def in_place_compress_left( arr ):
    cur_i = 0
    move_to = 0
    cur_val = None

    while cur_i < len( arr ):
        print( "Iteration %d" % cur_i )
        if cur_val is None:
            cur_val = arr[cur_i]

        elif cur_val == arr[cur_i]:
            print( "Assigning %d at position %d" % (cur_val * 2, move_to) )
            arr[move_to] = cur_val * 2
            cur_val = None
            move_to = move_to + 1

        elif arr[cur_i] is not None and cur_val != arr[cur_i]:
            print( "Assigning %d at position %d" % (cur_val, move_to) )
            arr[move_to] = cur_val
            cur_val = arr[cur_i]
            move_to = move_to + 1

        cur_i = cur_i + 1


    print( "Assigning %s at position %s" % (str(cur_val), str(move_to)) )
    arr[move_to] = cur_val
    move_to = move_to + 1

    while move_to < len( arr ):
        arr[move_to] = None
        move_to = move_to + 1

arr = [ 4, 2, 2, 2, None, 2, 2, 4, None, 8 ]
print( arr )
in_place_compress_left( arr )
print( arr )
