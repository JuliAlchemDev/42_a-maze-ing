from pydantic import BaseModel, Field
from enum import Enum


class ThemeType(Enum):
    DEFAULT = "default"
    DRACULA = "dracula"
    NORD = "nord"
    GRUVBOX = "gruvbox"
    SOLARIZED = "solarized"
    MONOKAI = "monokai"


class ValidateConfig(BaseModel):
    width: int = Field()
    height: int = Field()
    # entry: tuple[int, int] = Field()
    # exit: tuple[int, int] = Field()
    # output_file: str = Field()
    # perfect: bool = Field()
    # # seed: pass
    # algorithm: str = Field()
    # mode: ThemeType | None = Field(default=ThemeType.DEFAULT)
