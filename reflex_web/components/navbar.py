"""
This module contains the navbar component for the web application.
"""

import reflex as rx

import styles.styles as st
import styles.colors as color
import styles.fonts as font
import reflex_web.components.link_button as lb


def navbar() -> rx.Component:
    """
    Navbar component for the web application.
    :return: Component "navbar"
    """
    return rx.flex(
        rx.text(
            "Javier Curto",
            align="left",
            style=st.navbar_title_style,
        ),
        rx.flex(
            lb.link_navbar_button("INICIO", "/"),
            lb.link_navbar_button("SOBRE MI", "/"),
            lb.link_navbar_button("SKILLS", "/"),
            lb.link_navbar_button("CURRICULUM", "/"),
            lb.link_navbar_button("PORTFOLIO", "/"),
            lb.link_navbar_button("CONTACTO", "/"),
            spacing="5",
        ),
        position="sticky",
        top="0",
        bg=color.Colors.BG_SECONDARY.value,
        padding_x=st.Sizes.DEFAULT.value,
        padding_y=st.Sizes.SMALL.value,
        width=st.Percentages.FULL.value,
        z_index="999",
        justify="between",
        align="center",
        spacing="5",
    )
