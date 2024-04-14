import curses
from curses import wrapper
from curses.textpad import Textbox

import time

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_WHITE)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    
    GREEN_AND_WHITE = curses.color_pair(1)
    RED_AND_BLACK = curses.color_pair(2)

    x, y = 0, 0
    
    while True:
        key = stdscr.getkey()
        if key == "KEY_LEFT":
            x -= 1
        elif key == "KEY_RIGHT":
            x += 1
        elif key == "KEY_DOWN":
            y+= 1
        elif key == "KEY_UP":
            y -= 1
        stdscr.clear()
        stdscr.addstr(y, x, "0")
        stdscr.refresh()
        
    
    key = stdscr.getkey()
    stdscr.addstr(5,5, f"Key: {key}")
    stdscr.refresh()
    stdscr.getch()

wrapper(main)