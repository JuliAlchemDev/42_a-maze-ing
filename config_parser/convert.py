from typing import Any
from .errors import ConfigError


def to_int(key: str, value: str) -> int:
    try:
        return int(value)
    except ValueError:
        raise ConfigError(
            f"The {key} should be an integer!\n"
            f"  Received: '{value}'")


def to_coords(key: str, value: str) -> tuple[int, int]:
    parts = value.split(",")
    if len(parts) != 2:
        raise ConfigError(
            f"The {key} should have 2 integers, separated by one ','\n"
            f"  Received: {value}")

    x, y = parts
    return (to_int(key, x), to_int(key, y))


def to_bool(key: str, value: str) -> bool:
    normalized = value.strip().lower()

    if normalized not in ("true", "false"):
        raise ConfigError(
            f"The {key} should be True or False\n"
            f"  Received: {value}")
    return normalized == "true"


def convert_data(data: dict[str, str]) -> dict[str, Any]:
    converted: dict[str, Any] = {}
    for key, value in data.items():
        name = key.lower()
        if key in ("WIDTH", "HEIGHT", "SEED"):
            converted[name] = to_int(key, value)

        elif key in ("ENTRY", "EXIT"):
            converted[name] = to_coords(key, value)

        elif key == "PERFECT":
            converted[name] = to_bool(key, value)
        else:
            converted[name] = value
    return converted
