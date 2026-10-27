import sys


REQUIRED_KEYS = ["WIDTH", "HEIGHT", "ENTRY", "EXIT", "OUTPUT_FILE", "PERFECT"]
OPTIONAL_KEYS = ["SEED", "ALGORITHM", "MODE"]


class ConfigError(Exception):
    """Exception raised for configuration parsing errors."""
    pass


def validate_keys(config_keys: list):
    """
    === TODO: Validate key format and ensure only required or optional keys are present. ===

    Validate that all required configuration keys are present.

    Raises:
        ConfigError: If one or more required configuration keys are missing.

    Returns:
        ...
    """
    missing_keys = set(REQUIRED).difference(set(config_keys))
    if missing_keys:
        missing_keys_str = ", ".join(missing_keys)
        raise ConfigError(
                    f"missing data!\n"
                    f"REQUIRED: {missing_keys_str}"
                    )
    print(config_keys)


def parse_config(content: str):
    """
    === TODO: Return the parsed configuration data. ===

    Parse the configuration text into a dictionary.

    Raises:
        ConfigError: If the configuration format is invalid, duplicate
            keys are found, or required keys are missing.

    Returns:
        ...
    """

    lines = content.split("\n")

    config_data = {}
    for line in lines:
        if line == "" or line[0] == "#":
            continue

        parts = line.split("=")
        if len(parts) != 2 or parts[1] == "" or parts[0] == "":
            raise ConfigError(
                    f"invalid format!\n"
                    f"'{line}' should be 'KEY=VALUE'"
                    )

        key, value = parts
        if key in config_data.keys():
            raise ConfigError(
                    f"duplicate config key\n"
                    f"'{key}' already exists!"
                    )

        config_data.update({
            key: value
        })

    config_keys = [key for key in config_data]
    validate_keys(config_keys)
    # print(names_list)


def load_config():
    """
    === TODO: Return the parsed configuration data. ===
    Load and parse the configuration file provided as a command-line argument.

    Raises:
        ConfigError: If the number of arguments is incorrect or the file
        cannot be read or parsed.
    Returns:
        ...
    """

    argc = len(sys.argv)
    if (argc != 2):
        if (argc == 1):
            raise ConfigError("Provide at least 1 config file!")
        if (argc > 2):
            raise ConfigError("Provide only 1 config file!")
    else:
        config_data = sys.argv[1]
        try:
            with open(config_data, "r") as file:
                content = file.read()
                parse_config(content)
        except UnicodeDecodeError as error:
            raise ConfigError(
                f"decoding config file...\n"
                f"{error.reason.capitalize()}: '{config_data}'"
            )
        except OSError as error:
            raise ConfigError(
                f"reading config file...\n"
                f"{error.strerror}: '{error.filename}'"
                )


if __name__ == "__main__":
    load_config()
