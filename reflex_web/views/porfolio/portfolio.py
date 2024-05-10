"""
This module contains the portfolio component for the web application.
Currently, it only returns a text component with the string "Portfolio".
"""

import reflex as rx

import styles.styles as st
import styles.colors as color


def portfolio() -> rx.Component:
    """
    Returns a text component with the string "Portfolio".
    :return:    Component "Portfolio".
    """
    return rx.center(
        rx.text(
            "Porfolio",
            style=st.text_h1_title_style,
        ),
        id="portfolio",
        bg=color.Colors.BG_SECONDARY.value,
    )
