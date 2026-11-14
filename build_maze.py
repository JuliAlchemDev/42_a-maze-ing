import random

WALL, OPEN = 1, 0


def carve(width: int, height: int, seed: int | None = None,
          blocked: set[tuple[int, int]] | None = None) -> list[list[int]]:
    rng = random.Random(seed)
    blocked = blocked or set()
    grid = [[WALL] * (2 * width + 1) for _ in range(2 * height + 1)]
    visited = set(blocked)              # el 42 cuenta como "ya visitado"

    start = next((x, y) for y in range(height) for x in range(width)
                 if (x, y) not in blocked)
    stack = [start]
    visited.add(start)
    grid[2 * start[1] + 1][2 * start[0] + 1] = OPEN

    while stack:
        x, y = stack[-1]
        options = [(x + dx, y + dy) for dx, dy in ((0, -1), (1, 0), (0, 1), (-1, 0))
                   if 0 <= x + dx < width and 0 <= y + dy < height
                   and (x + dx, y + dy) not in visited]
        if options:
            nx, ny = rng.choice(options)
            grid[2 * y + 1][2 * x + 1] = OPEN
            grid[y + ny + 1][x + nx + 1] = OPEN      # el muro entre las dos
            grid[2 * ny + 1][2 * nx + 1] = OPEN
            visited.add((nx, ny))
            stack.append((nx, ny))
        else:
            stack.pop()
    return grid


def grid_to_hex(grid: list[list[int]]) -> list[str]:
    height, width = len(grid) // 2, len(grid[0]) // 2
    rows = []
    for y in range(height):
        row = ""
        for x in range(width):
            gx, gy = 2 * x + 1, 2 * y + 1
            value = (grid[gy - 1][gx] * 1      # N
                     + grid[gy][gx + 1] * 2    # E
                     + grid[gy + 1][gx] * 4    # S
                     + grid[gy][gx - 1] * 8)   # W
            row += f"{value:X}"
        rows.append(row)
    return rows


if __name__ == "__main__":
    # maze = carve(10, 8, seed=1)
    # maze = carve(10, 8, seed=2)
    # # maze = carve(10, 8, seed=1)


    # for row in maze:
    #     print(row)

    blocked = {(3, 2), (4, 2), (5, 2), (5, 3), (5, 4)}
    g = carve(10, 8, seed=1, blocked=blocked)
    for line in g:
        print("".join("██" if c else "  " for c in line))
    print(grid_to_hex(g))
