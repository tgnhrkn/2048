#!/usr/bin/python

from Strategy import *
from Game import Standard2048Game, GameTracker
import sys, inspect

argc = len( sys.argv )
if argc <= 1:
    print( "play.py <strategy> [rounds=XXX] [width=XXX] [height=XXX]" )
    sys.exit()

print( "Loading Strategies..." )
strategies = dict( filter(lambda x: inspect.isclass(x[1]), inspect.getmembers(sys.modules[ "Strategy" ] ) ) )

if sys.argv[1] not in strategies:
    print( "Strategy '%s' not found in Strategy.py" % sys.argv[1] )
    sys.exit()

picked = strategies[ sys.argv[1] ]

print( "Parsing Arguments..." )
arg_dict = {
    'rounds': 1,
    'width': 4,
    'height': 4,
    'csv_file': "2048.csv",
    }

toggle_dict = {
    'averages': False,
    'turns': False,
    'points': False,
    'csv': False,
    'print_finals': True,
}


for arg in sys.argv[2:]:
    
    if "=" not in arg and arg in toggle_dict:
        toggle_dict[ arg ] = not toggle_dict[ arg ]
        continue

    splt = arg.split( "=" , 1)
    if len( splt ) != 2:
        print( "Malformed arg: %s" % arg )
        sys.exit()
    if splt[ 0 ] not in arg_dict:
        print( "Unexpected arg: %s" % splt[0] )
        sys.exit()
    arg_dict[ splt[0] ] = type( arg_dict[splt[0]] )( splt[1] )

print( "Playing %d Round%s..." % (arg_dict['rounds'], "s" if arg_dict['rounds'] > 1 else "" ) )
game = Standard2048Game( strategy=picked(), width=arg_dict['width'], height=arg_dict['height'] )
tracker = GameTracker( game, rounds=arg_dict[ 'rounds' ] )
tracker.run()

if toggle_dict[ 'averages' ]:
    avgs = tracker.averages()
    if toggle_dict[ 'points' ]:
        print( "Average PPG: %d points" % avgs['points_avg'] )
    if toggle_dict[ 'turns' ]:
        print( "Average TPG: %d turns" % avgs['turns_avg'] )

print( "Done" )
