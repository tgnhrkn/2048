#!/usr/bin/python3
from HumanStrategy import HumanStrategy
from Game import Standard2048Game
import curses
from sys import argv


def main(stdscr):
    width = 4
    if len( argv ) == 2:
        width = int( argv[1] )
    stdscr.nodelay(1)
    ret = Standard2048Game( HumanStrategy( stdscr ), width=width ).play()
    stdscr.addstr( 0, 0, ret )
    stdscr.addstr( "Press 'l' to leave" )
    while stdscr.getch() != ord('l'):
        continue

if __name__ == '__main__':
    curses.wrapper(main)
