"""
This module contains the font constants for the application.
"""

from enum import Enum


class Font(Enum):
    """
    This class contains the font constants
    """
    DEFAULT = "Poppins"
    TITLE = "Poppins"
    LOGO = "Righteous"
    TEXT = "Poppins"


class FontWeight(Enum):
    """
    This class contains the font weight constants
    """
    LIGHT = "300"
    MEDIUM = "500"
    BOLD = "700"
