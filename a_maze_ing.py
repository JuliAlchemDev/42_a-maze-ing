from config_parser import load_config


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
        print(f"\nError: {error}\n")


if __name__ == "__main__":
    main()
