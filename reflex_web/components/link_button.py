"""
This module contains the link_button component for the web application.
It returns a link that is external.
"""

import reflex as rx


def link_button(text: str, url: str) -> rx.Component:
    """
    This function returns a link button that is external.
    :param text: The text to display on the button
    :param url: The url to link to
    :return: A link button that is external
    """
    return rx.link(
        rx.button(text),
        href=url,
        is_external=True
    )
