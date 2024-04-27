"""
This module contains the navbar component for the web application.
"""

import reflex as rx


def navbar() -> rx.Component:
    """
    Navbar component for the web application.
    :return: Component "navbar"
    """
    return rx.hstack(
        rx.text(
            "Javier Curto",
            height="50px",
            color="rgb(209, 150, 23)"
        ),
        position="sticky",
        bg="#1e2326",
        padding_x="16px",
        padding_y="8px",
        width="100%",
        z_index="999",
    )
