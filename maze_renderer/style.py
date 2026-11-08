"""Colors and ANSI codes used to paint the maze in the terminal."""

""" TODO: manage light / dark theme """

# Design system
BG_CLR = (14, 20, 30)
WALL_CLR = (110, 128, 156)
START_CLR = (200, 110, 220)
END_CLR = (235, 105, 120)
PATH_CLR = (80, 215, 245)
BLOCK_CLR = (205, 212, 228)

RESET = "\033[0m"
BOLD = "\033[1m"


"""
\033[ 48;2;R;G;B m
  │   │  │       └─ m: end of the command
  │   │  └───────── 2 = RGB mode
  │   └──────────── 48 = background (38 = text)
  └────────────---- \033[: start of the command
"""


def bg(color: tuple[int, int, int]) -> str:
    """
    Return the ANSI code that sets the background color.

    Args:
        color: (r, g, b) values from 0 to 255

    Returns:
        Escape sequence, e.g. "\033[48;2;14;20;30m"
    """
    r, g, b = color
    return f"\33[48;2;{r};{g};{b}m"


def text(color: tuple[int, int, int]) -> str:
    """
    Return the ANSI code that sets the text color.

    Args:
        color: (r, g, b) values from 0 to 255

    Returns:
        Escape sequence, e.g. "\033[38;2;14;20;30m"
    """
    r, g, b = color
    return f"\33[38;2;{r};{g};{b}m"
