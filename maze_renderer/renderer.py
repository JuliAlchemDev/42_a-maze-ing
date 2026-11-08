import time

from .constants import WALL, START, END, PATH
from .maze_grid import build_grid, build_maze, set_cell_value, set_path
from .style import RESET, BG_CLR, WALL_CLR, START_CLR, END_CLR, PATH_CLR, bg


def render_grid(maze_grid: list[list[int]]) -> None:
    """
    Print the grid in the terminal, one color per square.

    Each square is two characters wide so it looks square.
    OPEN squares (and any unknown value) use the background color.

    Args:
        maze_grid: matrix of grid values (WALL, OPEN, START, END, PATH)
    """
    for row in maze_grid:
        for col in row:
            if (col == WALL):
                print(f"{bg(WALL_CLR)}  {RESET}", end="")
            elif (col == START):
                print(f"{bg(START_CLR)}  {RESET}", end="")
            elif (col == END):
                print(f"{bg(END_CLR)}  {RESET}", end="")
            elif (col == PATH):
                print(f"{bg(PATH_CLR)}  {RESET}", end="")
            else:
                print(f"{bg(BG_CLR)}  {RESET}", end="")
        print()


def render_maze() -> None:
    """
    Build the maze step by step and show each stage in the terminal.

    === === TODO === ===
    1. Check this case!
        end = (0, 0)
        start = (1, 2)
    ...

    === === END TODO === ===

    """
    width = 2  # get from config
    height = 3  # get from config
    start = (0, 0)  # get from config
    end = (1, 2)  # get from config
    rows = ["D3", "96", "C7"]  # get from maze_generator
    path = "ESWSE"  # get from maze_solver

    grid = build_grid(width, height)
    render_grid(grid)

    maze = build_maze(rows)
    time.sleep(0.2)
    print(f"\033[{len(grid)}A", end="", flush=True)
    render_grid(maze)

    grid_with_start = set_cell_value(maze, start, START)
    time.sleep(0.2)
    print(f"\033[{len(grid)}A", end="", flush=True)
    render_grid(grid_with_start)

    grid_with_end = set_cell_value(maze, end, END)
    time.sleep(0.2)
    print(f"\033[{len(grid)}A", end="", flush=True)
    render_grid(grid_with_end)

    with_path = set_path(maze, start, path)
    time.sleep(0.2)
    print(f"\033[{len(grid)}A", end="", flush=True)
    render_grid(with_path)
