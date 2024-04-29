"""
This module contains the footer component for the web application.
It includes the current year, a link to website, and links profiles.
"""

import datetime as dt

import reflex as rx

import styles.styles as st
import styles.colors as color
from reflex_web.components.link_button import link_social_button


def footer() -> rx.Component:
    """
    Footer component for the web application.
    :return: Component with the footer of the web application.
    """
    current_year = str(dt.datetime.now().year)
    url = "https://jcurto.eu"

    return rx.hstack(
        rx.text(
            f"\u24b8 2023-{current_year} ",
            color=color.Colors.PRIMARY.value,
            font_size=st.Sizes.DEFAULT.value,
        ),
        rx.link(
            "Javier Curto Brull",
            href=url,
            color=color.Colors.SECONDARY.value,
            font_size="1.2em",
            font_weight="bold",
        ),
        link_social_button(
            "linkedin.svg", "https://www.linkedin.com/in/javier-curto-brull/"
        ),
        link_social_button("github.svg", "https://github.com/CurtoBrull"),
        link_social_button(
            "instagram.svg", "https://www.instagram.com/j.curtobrull/"),
        rx.image(
            src="favicon.ico",
            width=50,
            height=50,
            alt="favicon"
        ),
        bg=color.Colors.BG_SECONDARY.value,
        padding_x=st.Sizes.DEFAULT.value,
        padding_y=st.Sizes.SMALL.value,
        width=st.Percentages.FULL.value,
        position="sticky",
        bottom="0",
        z_index="999",
    )
