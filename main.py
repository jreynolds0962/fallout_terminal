from app.loading_screen import load
from curses import wrapper

def main(stdscr):
    load(stdscr)
    stdscr.clear()
    stdscr.getch()
    
wrapper(main)