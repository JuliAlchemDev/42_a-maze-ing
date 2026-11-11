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

    def __init__(self, x: int, y: int, walls: dict[str, int], height: int,
                 width: int, start: bool, end: bool, mark_42: bool) -> None:
        self.start = start
        self.end = end
        self.correct_path = False
        self.x = x
        self.y = y
        self.sign_42 = mark_42
        self.hex_rep = ""
        self.walls = walls
        self.dead_end = False
        if (x == 0):
            self.x_limit = 1
        elif (x >= width):
            self.x_limit = -1
        else:
            self.x_limit = 0
        if (y == 0):
            self.y_limit = 1
        elif (y >= height):
            self.y_limit = -1
        else:
            self.y_limit = 0

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

if __name__ == "__main__":
    x: int
    y: int
    width: int
    height: int
    start: bool
    end: bool
    mark_42: bool
    test_unit: Cell
    walls = dict[str, int]
    actual_cell: Cell
    rand_number: int
    board: list[list[Cell]]
    board_row: list[Cell]
    board_printer: list[str]
    aux_list: list[str]

    walls = {"N": 0, "E": 0, "S": 1, "W": 1}
    print("Start a cell tests!")
    print("Lets create a cell with values:")
    for wall, state in walls.items():
        print(f"Wall {wall} is {"open" if state == 1 else "closed"}")
    x = 1
    y = 1
    width = 5
    height = 5
    start = False
    end = False
    mark_42 = False
    try:
        print(f"The maze is {width}x{height} sized")
        print(f"This cell is on the [X:{x} Y:{y}] position.")
        print(f"The cell is start: {start}")
        print(f"The cell is end: {end}")
        print(f"The cell is 42: {mark_42}\n")
        print("Lets create the cell")
        test_unit = Cell(x, y, walls, height, width, start, end, mark_42)
        print("Cell created correctly")
        print("--------------------")
        print("Cell show info")
        test_unit.showInfo()
        print("--------------------")
        test_unit.cell_to_hex()
        print("--------------------")
        test_unit.print_cell()
        print("--------------------")
        print("Finished testing actual cell")
        print("Let's start trying a little board")

        board = []

        for x in range(width):
            board_row = []
            for y in range(height):
                cell_walls = {wall: rand.randint(0, 1) for wall in walls}
                board_row.append(Cell(x, y, cell_walls, height, width, start, end, mark_42))
            board.append(board_row)
        
        for x in range(0, width - 1):
            for y in range(0, height - 1):
                actual_cell = board[x][y]
                rand_number = rand.randint(0,100)
                if 30 > rand_number:
                    actual_cell.correct_path = True
                elif 90 < rand_number:
                    actual_cell.dead_end = True
        
        board_printer=[]
        for x in range(0, width):
            aux_list = ["","",""]
            for y in range(0, height):
                actual_cell = board[x][y]
                aux_list[0] = aux_list[0] + actual_cell.print_cell(0)
                aux_list[1] = aux_list[1] + actual_cell.print_cell(1)
                aux_list[2] = aux_list[2] + actual_cell.print_cell(2)
            board_printer.append(aux_list)

        print("=======================")
        for row in range(width):
            for line in range(3):
                print(board_printer[row][line])

        print("--------------------")
        print("--------------------")
    except Exception as e:
        print(f"Error while testing the cell: {e}")
    finally:
        print("Finished all tests")