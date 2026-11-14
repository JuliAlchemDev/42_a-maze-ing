import random


def show_grid(grid):
    for row in grid:
        print(row)
    print("====================")


def empty_grid(width: int, height: int) -> list[list[int]]:
    grid: list[list[int]] = []

    total_width = (width * 2) + 1
    total_height = (height * 2) + 1

    for _ in range(total_height):
        row = []
        for _ in range(total_width):
            row.append(1)
        grid.append(row)

    return grid


def open_cell(grid, x, y):
    grid[2*y+1][2*x+1] = 0


def open_wall(grid, x1, y1, x2, y2):
    y = y1 + y2 + 1
    x = x1 + x2 + 1
    grid[y][x] = 0


DIRS = {"N": (0, -1), "S": (0, 1), "E": (1, 0), "W": (-1, 0)}


def neighbors(
          x: int, y: int,
          width: int, height: int
          ) -> list[tuple[int, int]]:
    neighbors: list[tuple[int, int]] = []

    for dir in DIRS.values():
        dx, dy = dir
        nx = x + dx
        ny = y + dy
        if 0 <= nx < width and 0 <= ny < height:
            neighbors.append((dx + x, dy + y))

    return neighbors


def main():
    width = 2
    height = 3
    grid = empty_grid(width, height)

    # show_grid(grid)
    # TEST_1
    # for y in range(height):
    #     for x in range(width):
    #         open_cell(grid, x, y)
    # show_grid(grid)

    # open_wall(grid, 0, 0, 1, 0)
    # show_grid(grid)

    # print(neighbors(0, 0, 2, 3))
    # print(neighbors(1, 1, 2, 3))

    # TEST_2 DFS
    x, y = 0, 0
    visited = set()
    visited.add((x, y))
    open_cell(grid, x, y)

    # loop it!
    choices = []
    for cell in neighbors(x, y, width, height):
        if cell not in visited:
            choices.append(cell)

    nx, ny = random.choice(choices)

    open_cell(grid, nx, ny)
    open_wall(grid, x, y, nx, ny)
    visited.add((nx, ny))
    x, y = nx, ny
    show_grid(grid)

    choices = []
    for cell in neighbors(x, y, width, height):
        if cell not in visited:
            choices.append(cell)
    nx, ny = random.choice(choices)
    open_cell(grid, nx, ny)
    open_wall(grid, x, y, nx, ny)
    visited.add((nx, ny))
    x, y = nx, ny
    show_grid(grid)

    choices = []
    for cell in neighbors(x, y, width, height):
        if cell not in visited:
            choices.append(cell)
    nx, ny = random.choice(choices)
    open_cell(grid, nx, ny)
    open_wall(grid, x, y, nx, ny)
    visited.add((nx, ny))
    x, y = nx, ny
    show_grid(grid)


if __name__ == "__main__":
    main()
