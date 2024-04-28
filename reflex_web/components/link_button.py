"""
This module contains the link_button component for the web application.
It returns a link that is external.
"""

import reflex as rx


def link_button(icon: str, url: str) -> rx.Component:
    """
    This function returns a link button that is external.
    :param icon: The icon to display on the button
    :param url: The url to link to
    :return: A link button that is external
    """
    return rx.link(
        rx.icon(icon),
        href=url,
        is_external=True
    )


def link_button_text(text: str, url: str) -> rx.Component:
    """
    This function returns a link button that is external.
    :param text: The text to display on the button
    :param url: The url to link to
    :return: A link button that is external
    """
    return rx.link(
        rx.hstack(
            rx.button(
                rx.icon(text),
                href=url,
                is_external=True,
            ),
        )
    )
