"""
This file contains the constants used in the application
"""
from enum import Enum

import reflex as rx
import styles.colors as color
import styles.fonts as font

# Constants
MAX_WITH = "600px"


class Sizes(Enum):
    """
    This class contains the spacing constants
    """
    VERY_BIG = "4em"
    BIG = "2em"
    LARGE = "1.5em"
    MEDIUM = "1.25em"
    DEFAULT = "1em"
    SMALL = ".5em"


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
    "font_family": font.Font.DEFAULT.value,
    "background_color": color.Colors.BG.value,
    rx.button: {
        "height": "2.5em",
    },
    rx.text: {
        "font_family": "Righteous, sans-serif",
        "color": color.Colors.WHITE.value,
    },
    rx.list: {
        "color": color.Colors.WHITE.value,
    }
}

navbar_title_style = dict(
    font_family=font.Font.LOGO.value,
    font_weight=font.FontWeight.BOLD.value,
    font_size=Sizes.LARGE.value
)

text_h1_title_style = dict(
    font_size=Sizes.BIG.value,
    font_weigh=font.FontWeight.BOLD.value,
    margin="0",
    padding="0",
)

text_h2_style = dict(
    font_size=Sizes.LARGE.value,
    font_weigh=font.FontWeight.BOLD.value,
    margin="0",
    padding="0",
    color=color.Colors.PRIMARY.value
)

text_h3_style = dict(
    font_size=Sizes.MEDIUM.value,
    font_weigh="bold",
    margin="0",
    padding="0",
    color=color.Colors.WHITE.value
)

list_text_title = dict(
    color=color.Colors.PRIMARY.value,
    font_weigh="bold",
)

text_card_subs = dict(
    size="1",
    color=color.Colors.WHITE.value,
    align="center",
    width=Percentages.FULL.value,
    margin_bottom=Sizes.DEFAULT.value,
)
