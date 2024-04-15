from .TypeWriter import type_writer

WELCOME = """
WELCOME TO ROBCO INDUSTRIES (TM) TERMLINK\n\n
>SET TERMINAL/INQUIRE\n\n
RIT-V300\n\n
>SET FILE/PROTECTION=OWNER:RWED ACCOUNTS.F
>SET HALT RESTART/MAIN
"""

def load(stdscr):
    stdscr.clear()
    type_writer(stdscr, 0, WELCOME)
