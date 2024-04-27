"""
This module contains the skills component for the web application.
Currently, it only returns a text component with the string "Skills".
"""

import reflex as rx


def skills() -> rx.Component:
    """
    Returns a text component with the string "Skills".
    :return: Component "Skills"
    """
    return rx.text("Skills")
