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
            style=st.navbar_title_style,
        ),
        rx.flex(
            lb.link_navbar_button("SOBRE MI", "/#aboutme"),
            lb.link_navbar_button("SKILLS", "/#skills"),
            lb.link_navbar_button("CURRICULUM", "/#cv"),
            lb.link_navbar_button("PORTFOLIO", "/#portfolio"),
            lb.link_navbar_button("CONTACTO", "/#contact"),
            spacing="5",
            id="navbar-links",
            display=["none", "none", "flex", "flex"],
        ),
        id="navbar",
        position="sticky",
        top="0",
        z_index="999",
        padding_x=st.Sizes.SMALL.value,
        width=st.Percentages.FULL.value,
        bg=color.Colors.BG_SECONDARY.value,
        spacing="5",
        justify="between",
        align="baseline",
    )
