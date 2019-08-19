#!/usr/bin/python3

import curses
from Game import Standard2048Game
from MonteCarlo import MonteCarloVizStrategy


def main( win ):
    result = Standard2048Game( MonteCarloVizStrategy(win, 300, parallel=True, n_proc=10 ) ).setup_and_play()
    win.clear()
    win.refresh()
    curses.setsyx(0,0)
    for x in [ 'points', 'max', 'turns', 'endstr' ]:
        win.addstr("%s : %s\n" % (x, str(result[x]) ) )
    win.addstr( "Press 'l' to leave" )
    while win.getch() != ord('l'):
        continue

if __name__ == '__main__':
    curses.wrapper(main)
