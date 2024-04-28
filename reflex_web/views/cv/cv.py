"""
This module contains the cv component for the web application.
Currently, it only returns a text component with the string "Currículum".
"""

import reflex as rx

import styles.styles as st


def cv() -> rx.Component:
    """
            This function returns a component "CV".
            :return Component: "Currículum".
            """
    return rx.center(
        rx.text(
            "Currículum",
            style=st.text_h1_title_style,
        ),
        bg=st.Colors.BG,
    )
