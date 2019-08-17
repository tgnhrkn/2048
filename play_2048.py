#!/usr/bin/python3
from HumanStrategy import HumanStrategy
from Game import Standard2048Game
import curses
from sys import argv


def main(win):
    width = 4
    if len( argv ) == 2:
        width = int( argv[1] )
    win.nodelay(1)
    result = Standard2048Game( HumanStrategy( win ), width=width ).setup_and_play()
    for x in [ 'points', 'max', 'turns', 'endstr' ]:
        win.addstr("%s : %s\n" % (x, str(result[x]) ) )
    win.addstr( "Press 'l' to leave" )
    while win.getch() != ord('l'):
        continue

if __name__ == '__main__':
    curses.wrapper(main)
