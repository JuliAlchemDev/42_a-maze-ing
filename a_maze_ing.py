from config_parser import load_config


RESET = "\033[0m"
ERROR = "\033[38;2;235;105;120m"


def text(color: str) -> str:
    return color


def paint(content: str, color: str) -> str:
    return f"{text(color)}{content}{RESET}"


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
        load_config()
    except Exception as error:
        print(paint(f"\nError: {error}\n", ERROR))


if __name__ == "__main__":
    main()
