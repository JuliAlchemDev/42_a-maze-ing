from .constants import OPEN, WALL, PATH, MOVES

Grid = list[list[int]]


def maze_size(rows: list[str]) -> tuple[int, int]:
    height = len(rows)
    width = len(rows[0])
    return width, height


def build_grid(width: int, height: int) -> Grid:
    """
    Create a grid with all walls raised.

    Each cell is surrounded by walls, so the grid has
    (2 * height + 1) rows and (2 * width + 1) columns.

    Args:
        width: maze width in cells
        height: maze height in cells

    Returns:
        Grid filled with WALL, e.g. 2x3 cells -> 7 rows of 5 columns
    """
    grid = []
    grid_w = (width * 2) + 1
    grid_h = (height * 2) + 1
    for y in range(grid_h):
        row = []
        for x in range(grid_w):
            row.append(WALL)
        grid.append(row)
    return grid


def cell_to_grid(x: int, y: int) -> tuple[int, int]:
    """
    Convert maze cell coordinates to grid coordinates.

    Each cell is followed by a wall square, so cell k
    is drawn at position 2 * k + 1 in the grid.

    Args:
        x: cell column (0 is the first cell)
        y: cell row (0 is the first cell)

    Returns:
        (gx, gy): column and row in the grid
        e.g. cell (0, 0) -> (1, 1), cell (1, 2) -> (3, 5)
    """
    x = 2 * x + 1
    y = 2 * y + 1
    return (x, y)


def set_cell_value(
        grid: list[list[int]],
        coords: tuple[int, int],
        value: int) -> Grid:
    """
    Set a value in the grid at the given cell coordinates.

    Args:
        grid: matrix of grid values
        coords: (x, y) cell coordinates
        value: value to store (e.g. START, END, PATH)

    Returns:
        The same grid, modified in place, with the value set
    """
    x, y = coords
    gx, gy = cell_to_grid(x, y)
    grid[gy][gx] = value
    return grid


def set_path(
        grid: list[list[int]],
        start: tuple[int, int],
        path: str) -> Grid:
    """
    Mark the solution path in the grid.

    Each letter moves two squares: first the open wall between
    two cells, then the next cell. Only OPEN squares are changed,
    so START and END keep their value.

    Args:
        grid: matrix of grid values
        start: (x, y) cell coordinates of the entry
        path: moves as a string of N, E, S, W (e.g. "ESWSE")

    Returns:
        The same grid, modified in place, with PATH values set
    """
    x, y = cell_to_grid(start[0], start[1])
    moves = [MOVES[way] for way in path]
    for step_x, step_y in moves:
        for _ in range(2):
            x += step_x
            y += step_y
            if (grid[y][x] == OPEN):
                grid[y][x] = PATH

    return grid


def hex_to_digit(maze: list[str]) -> Grid:
    """
    Convert rows of hexadecimal digits into rows of numbers.

    Each character is one cell, and its four bits tell which
    walls are closed (N=1, E=2, S=4, W=8).

    Args:
        rows: one string per row, e.g. ["D3", "96", "C7"]

    Returns:
        Matrix of cell values, e.g. [[13, 3], [9, 6], [12, 7]]
    """
    cells = []
    for row in maze:
        colls = []
        for c in row:
            colls.append(int(c, 16))
        cells.append(colls)
    return cells


def build_maze(rows: list[str]) -> Grid:
    """
    Build the grid of a maze from its hexadecimal rows.

    Start with all walls raised, then open each cell and the
    walls to the east and south that its bits leave open.

    Args:
        rows: one string per row, one hex digit per cell

    Returns:
        Grid of (2 * height + 1) rows and (2 * width + 1) columns
    """
    cells = hex_to_digit(rows)
    height = len(cells)
    width = len(cells[0])
    grid = build_grid(width, height)

    for y in range(height):
        for x in range(width):
            gx, gy = cell_to_grid(x, y)
            grid[gy][gx] = OPEN
            if (cells[y][x] & 2) == 0:
                grid[gy][gx + 1] = OPEN
            if (cells[y][x] & 4) == 0:
                grid[gy + 1][gx] = OPEN

    return grid
