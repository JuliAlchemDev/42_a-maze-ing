import random

from maze_data import MazeData
from maze_renderer import render_interface

# TODO: replace mocks and regenerate() with parser, generator and solver

MOCK_2X3 = MazeData(
    start=(0, 0),  # get from config
    end=(1, 2),  # get from config
    rows=["D3", "96", "C7"],  # get from maze_generator
    path="ESWSE"  # get from maze_solver
)

MOCK_10X8 = MazeData(
    start=(0, 0),  # get from config
    end=(9, 7),  # get from config
    rows=[
        "D539553953", "93C6D3C6BA", "AC5392952A",
        "AD546EC3C6", "A955513AD3", "869396EA92",
        "C56AC53C6A", "D55457C556"],  # get from maze_generator
    path="EESENEEESENEESSSWNWWSESSSENESS"  # get from maze_solver
)


def regenerate() -> MazeData:
    print("TODO: regenerate maze data!")
    maze = random.choice([MOCK_2X3, MOCK_10X8])
    return maze


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

    try:
        render_interface(MOCK_2X3, regenerate)
    except Exception as error:
        print(f"\nError: {error}\n")


if __name__ == "__main__":
    main()
