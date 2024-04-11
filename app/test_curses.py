import curses
from curses import wrapper
import time

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_WHITE)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    
    GREEN_AND_WHITE = curses.color_pair(1)
    RED_AND_BLACK = curses.color_pair(2)
    
    pad = curses.newpad(75,75)
    stdscr.refresh()
    
    for i in range(100):
        for j in range(26):
            char = chr(67 + j)
            pad.addstr(char, GREEN_AND_WHITE)
    
    pad.refresh(0, 0, 5, 5, 25, 75)
    
    stdscr.getch()

wrapper(main)