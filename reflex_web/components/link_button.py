"""
This module contains the link_button component for the web application.
It returns a link that is external.
"""

import reflex as rx
import styles.colors as color


def link_social_button(image: str, url: str) -> rx.Component:
    """
    This function returns a link button.
    :param icon: The icon to display on the button
    :param url: The url to link to
    :return: A link button
    """
    return rx.link(
        rx.image(
            src=f"icons/{image}"
        ),
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


def link_navbar_button(text: str, link: str) -> rx.Component:
    """
    This function returns a link button.
    :return: A link button
    """
    return rx.link(
        text,
        href=f"{link}",
        is_external=False,
        color=color.Colors.WHITE.value,
    )
