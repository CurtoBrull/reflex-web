"""
This module contains the contact component for the web application.
Currently, it only returns a text component with the string "Contacto".
"""

import reflex as rx

import styles.styles as st
import styles.colors as color


def contact() -> rx.Component:
    """
        This function returns a component "Contact".
        :return rx.Component: "Contacto".
        """
    return rx.center(
        rx.text(
            "Contacto",
            style=st.text_h1_title_style,
        ),
        bg=color.Colors.BG.value,
    )
