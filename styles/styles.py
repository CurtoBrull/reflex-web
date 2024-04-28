"""
This file contains the constants used in the application
"""
from enum import Enum

import reflex as rx

# Constants
MAX_WITH = "600px"


class Spacing(Enum):
    """
    This class contains the spacing constants
    """
    BIG = "2em"
    H2 = "1.5em"
    H3 = "1.25em"
    DEFAULT = "1em"
    SMALL = ".5em"


class Colors(Enum):
    """
    This class contains the color constants
    """
    PRIMARY = "rgb(209, 150, 23)"
    SECONDARY = "rgb(209, 150, 23)"
    BG = "#1e2326"
    BG_SECONDARY = "#374046"
    SUCCESS = "#28a745"
    DANGER = "#dc3545"
    WARNING = "#ffc107"
    INFO = "#17a2b8"
    LIGHT = "#f8f9fa"
    DARK = "#343a40"
    WHITE = "#ffffff"
    BLACK = "#000000"
    GREY = "#6c757d"
    TRANSPARENT = "transparent"


class Percentages(Enum):
    """
    This class contains the percentage constants
    """
    FULL = "100%"
    HALF = "50%"
    THIRD = "33.33%"
    QUARTER = "25%"
    TENTH = "10%"
    FIVE = "5%"


BASE_STYLE = {
    rx.button: {
        "height": "2.5em",
    },
    rx.text: {
        "font_family": "Righteous, sans-serif",
        "color": Colors.WHITE,
    },
    rx.list: {
        "color": Colors.WHITE,
    }
}

text_h1_title_style = dict(
    font_size=Spacing.BIG,
    font_weigh="bold",
    margin="0",
    padding="0",
)

text_h2_style = dict(
    font_size=Spacing.H2,
    font_weigh="bold",
    margin="0",
    padding="0",
    color=Colors.PRIMARY
)

text_h3_style = dict(
    font_size=Spacing.H3,
    font_weigh="bold",
    margin="0",
    padding="0",
    color=Colors.WHITE
)

list_text_title = dict(
    color=Colors.PRIMARY,
    font_weigh="bold",
)

text_card_subs = dict(
    size="1",
    color=Colors.WHITE,
    align="center",
    width=Percentages.FULL,
    margin_bottom=Spacing.DEFAULT
)
