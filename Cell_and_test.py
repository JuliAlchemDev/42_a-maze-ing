import random as rand

class Cell():
    start: bool
    end: bool
    dead_end: bool
    correct_path: bool
    sign_42: bool
    forward: bool
    hex_rep: str
    x: int
    y: int
    x_limit: int
    y_limit: int
    walls: dict[str, int]
    times_configured: int

    def __init__(self, x: int, y: int, walls: dict[str, int], height: int,
                 width: int, start: bool, end: bool, mark_42: bool) -> None:
        self.x = x
        self.y = y
        self.hex_rep = ""
        self.x_limit = 1 if x == 0 else ( -1 if x >= width else 0)
        """
        if (x == 0):
            self.x_limit = 1
        elif (x >= width):
            self.x_limit = -1
        else:
            self.x_limit = 0
        """
        self.y_limit = 1 if x == 0 else ( -1 if x >= width else 0)
        """
        if (y == 0):
            self.y_limit = 1
        elif (y >= height):
            self.y_limit = -1
        else:
            self.y_limit = 0
        """
        self.sign_42 = mark_42
        if mark_42:
            self.walls = {"N": 0, "S": 0, "E": 0, "W": 0}
            self.start = False
            self.end = False
            self.correct_path = False
            self.times_configured = -1
            self.dead_end = False
        else:
            self.walls = walls
            self.start = start
            self.end = end
            self.correct_path = False
            self.times_configured = 0
            self.dead_end = True if sum(self.walls.values()) >= 3 else False

    def cell_to_hex(self, force_conv: bool = False) -> str:
        requirements: list[str]
        aux_nbr: int

        if self.hex_rep != "" and not force_conv:
            return self.hex_rep
        requirements = ["N", "E", "S", "W"]
        aux_nbr = 0
        for wall in requirements:
            if not wall in self.walls.keys():
                self.walls[wall] = 0
            aux_nbr = (aux_nbr << 1) + self.walls[wall]
        print(self.hex_rep)
        print(aux_nbr)
        print(bin(aux_nbr))
        self.hex_rep = hex(aux_nbr)
        print(bin(aux_nbr).zfill(4))
        print(hex(aux_nbr).zfill(4))
        return ("X")
        
    def showInfo(self) -> None:
        print("\n\nvvvvvvvvvvvvvvvvvvvvvvvv\n")
        print("The Cell is the start") if self.is_start() else ""
        print("The Cell is the end") if self.is_end() else ""
        for wall, state in self.walls.items():
            print(f"Wall: {wall} is {"closed" if state == 1 else "open"}")
        print("The Cell is a dead end") if self.is_dead_end() else ""
        print("\n^^^^^^^^^^^^^^^^^^^^^^^^\n\n")

    def cell_content(self) -> str:
        return "@" if self.sign_42 else ("X" if self.dead_end else " ")

    def print_cell(self, row: int = -1) -> None | str:
        """
        print("·-=-·")
        print("||X||")
        print("·-=-·")
        """
        if row == -1:
            print("#-=-#") if self.walls['N'] == 0 else print("#   #")
            if self.walls["W"] == 0 and self.walls["E"] == 0:
                print(f"| {self.cell_content()} |")
            elif self.walls["W"] == 0:
                print(f"| {self.cell_content()}  ")
            else:
                print(f"  {self.cell_content()} |")
            print("#-=-#") if self.walls['S'] == 0 else print("#   #")
        elif row == 0:
            return "#-=-#" if self.walls['N'] == 0 else "#   #"
        elif row == 1:
            if self.walls["W"] == 0 and self.walls["E"] == 0:
                return f"| {self.cell_content()} |"
            elif self.walls["W"] == 0:
                return f"| {self.cell_content()}  "
            else:
                return f"  {self.cell_content()} |"
        elif row == 2:
            return "#-=-#" if self.walls['S'] == 0 else "#   #"
        

    def is_dead_end(self) -> bool:
        dead_count: int

        dead_count = 0
        for state in self.walls.values():
            dead_count = dead_count + state

        return (dead_count >= 3)
    
    def is_start(self) -> bool:
        return self.start

    def is_end(self) -> bool:
        return self.end
