"""
This module contains the navbar component for the web application.
"""

import reflex as rx

import styles.styles as st


def navbar() -> rx.Component:
    """
    Navbar component for the web application.
    :return: Component "navbar"
    """
    return rx.hstack(
        rx.text(
            "Javier Curto",
            height="50px",
            color=st.Colors.PRIMARY,
            align="center"
        ),
        position="sticky",
        top="0",
        bg=st.Colors.BG_SECONDARY,
        padding_x=st.Spacing.DEFAULT,
        padding_y=st.Spacing.SMALL,
        width=st.Percentages.FULL,
        z_index="999",
    )
