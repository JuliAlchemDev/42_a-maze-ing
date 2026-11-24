from enum import Enum
from typing import Self

from pydantic import BaseModel, Field, model_validator

from .errors import ConfigError


class ThemeType(Enum):
    DEFAULT = "default"
    DRACULA = "dracula"
    NORD = "nord"
    GRUVBOX = "gruvbox"
    SOLARIZED = "solarized"
    MONOKAI = "monokai"


class ValidateConfig(BaseModel):
    # Check reasonable limits
    width: int = Field(ge=2, le=100)
    height: int = Field(ge=2, le=100)
    entry: tuple[int, int] = Field()
    exit: tuple[int, int] = Field()
    output_file: str = Field()
    perfect: bool = Field()
    # Check negative seed
    seed: int | None = None
    # algorithm: str = Field()
    theme: ThemeType | None = Field(default=ThemeType.DEFAULT)

    @model_validator(mode="after")
    def validate_coords(self) -> Self:
        x_in, y_in = self.entry
        x_out, y_out = self.exit
        x_limit = self.width - 1
        y_limit = self.height - 1
        if self.entry == self.exit:
            raise ConfigError("ENTRY and EXIT should be different")

        if (x_in < 0 or x_in > x_limit or
                y_in < 0 or y_in > y_limit):
            raise ConfigError(
                f"ENTRY {self.entry} is outside the maze\n"
                "  Valid range: "
                f"x 0-{x_limit}, "
                f"y 0-{y_limit}")

        if (x_out < 0 or x_out > x_limit or
                y_out < 0 or y_out > y_limit):
            raise ConfigError(
                f"EXIT {self.exit} is outside the maze\n"
                "  Valid range: "
                f"x 0-{x_limit}, "
                f"y 0-{y_limit}")

        return self
