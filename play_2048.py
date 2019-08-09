#!/usr/bin/python3
from Strategy import HumanStrategy
from Game import Standard2048Game
import curses


def main(stdscr):
    stdscr.nodelay(1)
    ret = Standard2048Game( HumanStrategy( stdscr ) ).play()
    stdscr.addstr( 0, 0, ret )
    stdscr.addstr( "Press 'l' to leave" )
    while stdscr.getch() != ord('l'):
        continue

if __name__ == '__main__':
    curses.wrapper(main)
