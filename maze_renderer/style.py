"""Colors and ANSI codes used to paint the maze in the terminal."""

# Design system
THEMES = {
    "default": {
        "bg": (14, 20, 30),
        "wall": (110, 128, 156),
        "start": (200, 110, 220),
        "end": (235, 105, 120),
        "path": (80, 215, 245),
        "block": (205, 212, 228),
    },
    "dracula": {
        "bg": (40, 42, 54),
        "wall": (189, 147, 249),
        "start": (139, 233, 253),
        "end": (255, 184, 108),
        "path": (255, 121, 198),
        "block": (80, 250, 123),
    },
    "nord": {
            "bg": (46, 52, 64),
            "wall": (94, 129, 172),
            "start": (136, 192, 208),
            "end": (191, 97, 106),
            "path": (235, 203, 139),
            "block": (163, 190, 140),
        },
    "gruvbox": {
        "bg": (40, 40, 40),
        "wall": (146, 131, 116),
        "start": (142, 192, 124),
        "end": (251, 73, 52),
        "path": (250, 189, 47),
        "block": (235, 219, 178),
    },
    "solarized": {
        "bg": (0, 43, 54),
        "wall": (88, 110, 117),
        "start": (42, 161, 152),
        "end": (203, 75, 22),
        "path": (181, 137, 0),
        "block": (238, 232, 213),
    },
    "monokai": {
        "bg": (39, 40, 34),
        "wall": (117, 113, 94),
        "start": (102, 217, 239),
        "end": (249, 38, 114),
        "path": (166, 226, 46),
        "block": (253, 151, 31),
    },
}

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
