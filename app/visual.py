import time
import curses

def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_YELLOW)
    
    stdscr.attron(curses.color_pair(1))
    
    h, w = stdscr.getmaxyx()
    
    text = "Hello, World!"
    
    x = w // 2 - len(text) // 2
    
    y = h // 2
    
    stdscr.addstr(y, x, text)
    stdscr.refresh()
    time.sleep(3)
    
curses.wrapper(main)