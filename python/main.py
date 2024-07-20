import curses


def refresh_screen(stdscr, data, columns, cursor_x, cursor_y):
    curr_x = 0
    for wx in range(8):
        for wy in range(8):
            stdscr.move(wy, curr_x)
            if cursor_x == wx and cursor_y == wy:
                stdscr.addstr(data[wy][wx].ljust(columns[wx]), curses.color_pair(1))
                stdscr.addch(' ')
            else:
                stdscr.addstr(data[wy][wx].ljust(columns[wx]) + ' ')
        curr_x += columns[wx] + 1


def get_column_width(data, col_x):
    longest = 0
    for wy in range(8):
        curr_str = data[wy][col_x]
        if len(curr_str) > longest:
            longest = len(curr_str)
    return longest


def main(stdscr):

    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    columns = [1, 1, 1, 1, 1, 1, 1, 1]
    data = [['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']]

    cursor_x = 0
    cursor_y = 0

    refresh_screen(stdscr, data, columns, 0, 0)
    should_exit = False
    while not should_exit:
        last_key = stdscr.getch()
        if last_key == curses.KEY_UP:
            cursor_y -= 1
        elif last_key == curses.KEY_DOWN:
            cursor_y += 1
        elif last_key == curses.KEY_LEFT:
            cursor_x -= 1
        elif last_key == curses.KEY_RIGHT:
            cursor_x += 1
        elif last_key == curses.KEY_DC:
            data[cursor_y][cursor_x] = ''
        elif last_key == curses.KEY_BACKSPACE:
            if len(data[cursor_y][cursor_x]) > 0:
                data[cursor_y][cursor_x] = data[cursor_y][cursor_x][:-1]
        elif last_key == curses.KEY_CLOSE:  # TODO
            return
        else:
            data[cursor_y][cursor_x] += chr(last_key)
        for col_x in range(8):
            columns[col_x] = get_column_width(data, col_x)
        refresh_screen(stdscr, data, columns, cursor_x, cursor_y)


curses.wrapper(main)