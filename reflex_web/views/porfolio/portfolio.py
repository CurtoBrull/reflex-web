"""
This module contains the portfolio component for the web application.
Currently, it only returns a text component with the string "Portfolio".
"""

import reflex as rx


def portfolio() -> rx.Component:
    """
    Returns a text component with the string "Portfolio".
    :return:    Component "Portfolio".
    """
    return rx.text("Porfolio")
