"""
This module contains the aboutme component for the web application.
Currently, it only returns a text component with the string "Sobre Mí".
"""

import reflex as rx


def aboutme() -> rx.Component:
    """
    Returns a text component with the string "Sobre Mí".
    :return: Component "Sobre Mí".
    """
    return rx.text("Sobre Mí")
