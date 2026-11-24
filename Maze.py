from Cell_and_test import Cell
import random as rand


class Maze():
    board: list[list[Cell]]
    start: tuple[int, int]
    end: tuple[int, int]
    sign_42: list[Cell]
    width: int
    height: int

    def __init__(self, width: int = 5, height: int = 5) -> None:
        self.board = []
        self.width = width
        self.height = height

    def print_maze_debug(self):
        board_printer: list[list[str]]
        aux_list: list[str]
        actual_cell: Cell

        board_printer=[]
        for x in range(0, self.width):
            aux_list = ["","",""]
            for y in range(0, self.height):
                actual_cell = self.board[x][y]
                aux_list[0] = aux_list[0] + str(actual_cell.print_cell(0))
                aux_list[1] = aux_list[1] + str(actual_cell.print_cell(1))
                aux_list[2] = aux_list[2] + str(actual_cell.print_cell(2))
            board_printer.append(aux_list)

        print("=======================")
        for row in range(self.width):
            for line in range(3):
                print(board_printer[row][line])

        print("--------------------")
        print("--------------------")

    def generate_random_no_logic(self, height: int, width: int):
        # TODO: Generate coherence
        board_row: list[Cell]
        cell_walls: dict[str, int]
        actual_cell: Cell

        self.width = width
        self.height = height
        for x in range(width):
            board_row = []
            for y in range(height):
                cell_walls = {wall: rand.randint(0, 1) for wall in ['N', 'S', 'W', 'E']}
                board_row.append(Cell(x, y, cell_walls, height, width, False, False, False))
            self.board.append(board_row)

        for x in range(0, width - 1):
            for y in range(0, height - 1):
                actual_cell = self.board[x][y]
                rand_number = rand.randint(0,100)
                if 30 > rand_number:
                    actual_cell.correct_path = True
                elif 90 < rand_number:
                    actual_cell.dead_end = True

    def get_board(self) -> list[list[Cell]]:
        return (self.board)

    def generate_empty_maze(self):
        pass

    def insert_42_signature(self):
        pass

    def generate_correct_path(self):
        pass

    """
    mode defines if we had no logic while making the full maze or what type.
    0: No logic, left to right, up to down priority
    1: As the filler exercise from start and end points
    2: From the 42
    3: From all cells from the path
    4: From full center
    """
    def apply_coherence(self, x: int, y: int, mode: int = 0):
        actual_cell: Cell
        other_cell: Cell
        # TODO: Implement the additional coherence modes.
        actual_cell = self.board[x][y]
        if not actual_cell.coherence_applied:
            actual_cell.coherence_applied = True
            # x advances down the printed rows; y advances across columns.
            if x < len(self.board) - 1:
                other_cell = self.board[x + 1][y]
                other_cell.walls["N"] = actual_cell.walls["S"]
            if x > 0:
                other_cell = self.board[x - 1][y]
                other_cell.walls["S"] = actual_cell.walls["N"]
            if y > 0:
                other_cell = self.board[x][y - 1]
                other_cell.walls["E"] = actual_cell.walls["W"]
            if y < len(self.board[x]) - 1:
                other_cell = self.board[x][y + 1]
                other_cell.walls["W"] = actual_cell.walls["E"]
            if x > 0:
                self.apply_coherence(x - 1, y, mode)
            if x < len(self.board) - 1:
                self.apply_coherence(x + 1, y, mode)
            if y > 0:
                self.apply_coherence(x, y - 1, mode)
            if y < len(self.board[x]) - 1:
                self.apply_coherence(x, y + 1, mode)

    # TODO: this will fill the correct path instead a full random logic
    def fill_maze(self, use_logic: bool = False):
        pass


def initial_test():
    x: int
    y: int
    width: int
    height: int
    start: bool
    end: bool
    mark_42: bool
    test_unit: Cell
    walls = dict[str, int]

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

    except Exception as e:
        print(f"Error while testing the cell: {e}")
    finally:
        print("Finished all tests")

if __name__ == "__main__":
    # initial_test()
    test_maze: Maze

    test_maze = Maze()
    test_maze.generate_random_no_logic(5, 5)
    test_maze.print_maze_debug()
    test_maze.apply_coherence(0, 0, 0)
    test_maze.print_maze_debug()