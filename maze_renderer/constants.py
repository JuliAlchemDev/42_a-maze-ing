"""Grid cell values and moves shared by the renderer modules."""

# Grid cell values
OPEN = 0
WALL = 1
START = 2
END = 3
PATH = 4
BLOCK = 5

# Moves per letter: (column step, row step)
MOVES = {"N": (0, -1), "E": (1, 0), "S": (0, 1), "W": (-1, 0)}
