#!/usr/bin/python3
from Game import Standard2048Game
from MonteCarlo import MonteCarloStrategy
import numpy as np
import sys
import time

np.seterr( invalid='raise' )

stime = time.time()
br = 1
if len( sys.argv ) == 2:
    br = int( sys.argv[1] )

result = Standard2048Game( MonteCarloStrategy( br ) ).setup_and_play()

ttime = time.time() - stime

for x in [ 'points', 'max', 'turns', 'endstr' ]:
    print("%s : %s" % (x, str(result[x]) ) )

print( "Finished in %d seconds" % ttime )
