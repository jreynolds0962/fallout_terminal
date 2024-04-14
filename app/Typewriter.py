import time

def type_writer(stdscr, y_axis: int, *args: str) -> None:
    """The function mimics a natural typing visual

    Args:
        stdscr (_type_): curses screen
        y_axis (int): the Y axis of curses window to start on
    """
    x_axis = 0
    for arg in args:
        arg.strip()
        for char in arg:
            stdscr.addstr(y_axis, x_axis, char)
            stdscr.refresh()
            if char != "\n":
                time.sleep(0.04)
                x_axis += 1
            else:
                time.sleep(0.3)
                y_axis += 1
                x_axis = 0