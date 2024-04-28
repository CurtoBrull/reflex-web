"""
This module contains the skills component for the web application.
Currently, it only returns a text component with the string "Skills".
"""

import reflex as rx

import styles.styles as st


def skills() -> rx.Component:
    """
    Returns a text component with the string "Skills".
    :return: Component "Skills"
    """
    return rx.center(
        rx.text(
            "Skills",
            style=st.text_h1_title_style,
        ),
        bg=st.Colors.BG,
    )
