"""
This module contains the navbar component for the web application.
"""

import reflex as rx

import styles.styles as st
import styles.colors as color


def navbar() -> rx.Component:
    """
    Navbar component for the web application.
    :return: Component "navbar"
    """
    return rx.hstack(
        rx.text(
            "Javier Curto",
            height="50px",
            color=color.Colors.PRIMARY.value,
            align="center"
        ),
        position="sticky",
        top="0",
        bg=color.Colors.BG_SECONDARY.value,
        padding_x=st.Sizes.DEFAULT.value,
        padding_y=st.Sizes.SMALL.value,
        width=st.Percentages.FULL.value,
        z_index="999",
    )
