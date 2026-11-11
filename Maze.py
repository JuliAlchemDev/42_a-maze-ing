from Cell_and_test import Cell
import random as rand


class Maze():
    board: list[list[Cell]]
    start: tuple[int, int]
    end: tuple[int, int]
    sign_42: list[Cell]

    def print_maze_debug(self):
        pass

    def generate_random_no_logic(self):
        # TODO: Generate coherence
        pass

    def generate_empty_maze(self):
        pass

    def insert_42_signature(self):
        pass

    def generate_correct_path(self):
        pass

    def fill_maze(self, use_logic: bool = False):
        pass



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