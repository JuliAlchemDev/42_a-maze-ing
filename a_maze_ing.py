from maze_renderer import render_maze


# class MazeData:
#     def __init__(self, start, end, rows, path):
#         self.start = start
#         self.end = end
#         self.rows = rows
#         self.path = path


def main() -> None:
    """
    === === TODO === ===

    [] - parse config.txt
    [] - generate maze
    [] - resolve maze
    [] - render maze
    ...
    === === END TODO === ===

    Load the configuration and handle related errors.

    Raises:
    Returns: ...
    """
    # maze2x3
    # width = 2  # get from config
    # height = 3  # get from config
    start = (0, 0)  # get from config
    end = (1, 2)  # get from config
    rows = ["D3", "96", "C7"]  # get from maze_generator
    path = "ESWSE"  # get from maze_solver

    # maze2x3 = MazeData()

    # maze10x8 = new MazeData()

    # while True:
    #     print("=== A-Maze-ing ===")
    #     print("1. Re-generate a new maze")
    #     print("2. Show / Hide the shortest path")
    #     print("3. Switch the color theme")
    #     print("4. Quit")
    #     choice = int(input("Choice? (1-4): "))

    #     if choice == 4:
    #         sys.exit()

    try:
        render_maze(start, end, rows, path)
    except Exception as error:
        print(f"\nError: {error}\n")


if __name__ == "__main__":
    main()
