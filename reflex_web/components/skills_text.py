"""
"""

import reflex as rx

import styles.styles as st
import styles.colors as color


def skills_list_item(title: str, desc: str) -> rx.Component:
    """
    Returns a list item with a title and a description.
    :param title: The title of the list item.
    :param desc: The description of the list item.
    :return: A list item with a title and a description.
    """
    return rx.list(
        rx.list.item(
            title,
            color=color.Colors.PRIMARY.value
        ),
        rx.list.item(desc),
        margin_bottom=st.Sizes.SMALL.value,
    )