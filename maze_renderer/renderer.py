# import os
import time
# from collections.abc import Callable # check if permitted
from typing import Callable

from maze_data import MazeData
from .constants import WALL, START, END, PATH, BLOCK
from .maze_grid import (
    maze_size, build_grid,
    build_maze, set_cell_value,
    set_path)

from .style import RESET, THEMES, bg, paint, block

Grid = list[list[int]]
FRAME_DELAY = 0.3


def render_grid(maze_grid: list[list[int]], theme: str) -> None:
    """
    Print the grid in the terminal, one color per square.

    Each square is two characters wide so it looks square.
    OPEN squares (and any unknown value) use the background color.

    Args:
        maze_grid: matrix of grid values (WALL, OPEN, START, END, PATH)
    """
    
    # TODO: refactor using paint and block funcs
    colors = THEMES[theme]

    for row in maze_grid:
        for col in row:
            if (col == WALL):
                print(f"{bg(colors['wall'])}  {RESET}", end="")
            elif (col == START):
                print(f"{bg(colors['start'])}  {RESET}", end="")
            elif (col == END):
                print(f"{bg(colors['end'])}  {RESET}", end="")
            elif (col == PATH):
                print(f"{bg(colors['path'])}  {RESET}", end="")
            elif (col == BLOCK):
                print(f"{bg(colors['block'])}  {RESET}", end="")
            else:
                print(f"{bg(colors['bg'])}  {RESET}", end="")
        print()


def rewind(height: int) -> None:
    """
    Move the cursor up to redraw over the previous frame.

    Uses the ANSI sequence ESC[nA, which only moves the cursor
    up n lines. It does not erase anything: the next render
    overwrites the old characters, so there is no flicker.

    Args:
        height: number of lines to move up (rows of the last
            frame drawn)
    """
    print(f"\033[{height}A", end="", flush=True)
    # print("\033[H", end="", flush=True)  # cursor_home


def play_frames(
        frames: list[Grid],
        theme: str,
        delay: float = FRAME_DELAY) -> None:
    """
    Show each frame in place, one after another.

    The first frame is printed as is; every following frame is
    drawn over the previous one by moving the cursor back up.
    All frames must have the same height.

    Args:
        frames: grids to display, in order
        theme: color theme name (a key of THEMES)
        delay: seconds to wait between frames
    """
    for i, frame in enumerate(frames):
        if i > 0:
            time.sleep(delay)
            rewind(len(frame))
        render_grid(frame, theme)


def render_maze(maze: MazeData) -> None:
    """
    Animate the maze being built, step by step.

    Frames: walls only, open maze, start, end and, if
    maze.show_path is set, the solution path.

    Args:
        maze: maze data (rows, start, end, path, theme)
    """
    theme = maze.theme.lower()
    width, height = maze_size(maze.rows)

    walls = build_grid(width, height)
    open_maze = build_maze(maze.rows)
    with_start = set_cell_value(open_maze, maze.start, START)
    with_end = set_cell_value(with_start, maze.end, END)

    frames = [walls, open_maze, with_start, with_end]
    if maze.show_path:
        frames.append(set_path(with_end, maze.start, maze.path))

    play_frames(frames, theme)


def show_legend(theme: str) -> None:
    """
    Print the color legend below the maze.

    Shows one color block per element (entry, exit, "42 pattern"
    and shortest path) followed by its label.

    Args:
        theme: color theme name (a key of THEMES, any case)
    """
    colors = THEMES[theme.lower()]
    items = [
        ("start", "entry"),
        ("end", "exit"),
        ("block", '"42 pattern"'),
        ("path", "shortest path")
    ]
    legend = "  ".join(
        f"{block(colors[key])} {paint(label, colors['wall'])}"
        for key, label in items
    )
    print(f"\n{legend}\n")


def show_menu(theme: str):
    """
    Print the title and the list of options below the maze.

    Args:
        theme: color theme name (a key of THEMES, any case)
    """
    menu_options = (
        "1. Re-generate a new maze",
        "2. Show / Hide the shortest path",
        "3. Switch the color theme",
        "4. Quit",
        )
    colors = THEMES[theme.lower()]
    print("=== A-Maze-ing ===\n")
    print(f"{paint('Theme:', colors['end'])} "
          f"{paint(theme.capitalize(), colors['path'])}")

    for line in menu_options:
        print(paint(line, colors['wall']))


def render_interface(
        maze: MazeData,
        regenerate: Callable[[], MazeData]
        ) -> None:
    """
    Run the interactive terminal menu until the user quits.

    Each loop clears the screen, draws the maze, the legend and
    the menu, and then waits for an option:
        1. Re-generate a new maze (calls regenerate)
        2. Show / hide the shortest path
        3. Switch to the next color theme
        4. Quit

    An invalid input (not a number, or outside 1-4) shows an error
    message under the menu on the next redraw. Ctrl+C and Ctrl+D
    also exit cleanly.

    Args:
        maze: maze to display; its show_path and theme fields are
            modified in place when the user toggles them
        regenerate: callable that returns a new MazeData, used by
            option 1 (a new maze replaces the current one)

    Returns:
        None. The function returns when the user quits.
    """
    error = ""
    while True:
        print("\033[2J\033[H", end="", flush=True)
        render_maze(maze)
        show_legend(maze.theme)
        show_menu(maze.theme)
        colors = THEMES[maze.theme.lower()]

        if error:
            print(paint(f"\n{error}\n", colors['end']))
            error = ""

        try:
            choice = int(input(
                paint("Choice? (1-4): ", colors['path'])).strip())
        except ValueError:
            error = "Please enter a number from 1 to 4"
            continue

        except (KeyboardInterrupt, EOFError):
            print()
            print("\nBye!\n")
            return

        if choice == 1:
            maze = regenerate()
        elif choice == 2:
            maze.show_path = not maze.show_path
        elif choice == 3:
            names = list(THEMES)
            i = names.index(maze.theme.lower())
            maze.theme = names[(i+1) % len(names)]
        elif choice == 4:
            print("\nBye!\n")
            return
        else:
            error = "Please enter a number from 1 to 4"
