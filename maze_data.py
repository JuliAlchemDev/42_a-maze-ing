class MazeData:
    """
    Maze information shared between modules.

    Attributes:
        start: (x, y) cell coordinates of the entry
        end: (x, y) cell coordinates of the exit
        rows: one hex string per row, one digit per cell
        path: shortest path as a string of N, E, S, W
        show_path: whether the path is visible
        theme: name of the color theme
    """
    def __init__(
            self, start: tuple[int, int],
            end: tuple[int, int],
            rows: list[str],
            path: str,
            show_path: bool = False,
            theme: str = "DEFAULT"):
        self.start = start
        self.end = end
        self.rows = rows
        self.path = path
        self.show_path = show_path
        self.theme = theme
