import curses
from curses import wrapper


def main(stdscr):
    inp = 0
    y, x = stdscr.getmaxyx()
    stdscr.clear()
    stdscr.nodelay(1)
    while inp != 48 and inp != 27:
        while True:
            try:
                text = "I AM KILL TERMINAL WHEN RESIZE AAAAAAAH"
                text_height, text_width = stdscr.getmaxyx()
                text_height = min(text_height, y - 5)  # move text down 5 rows
                text = text[:text_width]  # ensure text fits within screen width
                stdscr.addnstr(text_height, 0, text, text_width)
            except curses.error:
                pass
            inp = stdscr.getch()
            if inp != curses.KEY_RESIZE:
                break
            # handle zero or negative dimensions
            new_y, new_x = stdscr.getmaxyx()
            if new_y <= 0:
                new_y = y
            if new_x <= 0:
                new_x = x
            y, x = new_y, new_x
            curses.resize_term(y, x)  # resize to get the new screen dimensions
            stdscr.erase()
            stdscr.refresh()


wrapper(main)
