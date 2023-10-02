import curses
from curses import wrapper

def main(stdscr):
    stdscr.clear()
    stdscr.addstr(10,10,"hello term",curses.A_BOLD)
    stdscr.addstr(10,12,"overwritten")
    stdscr.addstr(15,25,"curses term")
    stdscr.refresh()
    stdscr.getch()

wrapper(main)
