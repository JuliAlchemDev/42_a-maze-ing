class MazeData:
    def __init__(
            self, start: tuple[int, int],
            end: tuple[int, int],
            rows: list[list[str]],
            path: str,
            show_path: bool = False,
            theme: str = "DEFAULT"):
        self.start = start
        self.end = end
        self.rows = rows
        self.path = path
        self.show_path = show_path
        self.theme = theme
