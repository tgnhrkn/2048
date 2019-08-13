#!/usr/bin/python3
from .Strategy import AllFourStrategy
from .Game import Standard2048Game
from sys import argv

width = 4
if len( argv ) == 2:
    width = int( argv[1] )

print( Standard2048Game( AllFourStrategy(), width=width ).play() )
