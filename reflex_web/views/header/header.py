"""
This module contains the header component for the web application.
It includes the avatar, name, role, skills, and social media links of the user.
"""

import reflex as rx
from libgravatar import Gravatar

import styles.styles as st
import styles.colors as color
from reflex_web.components.link_button import link_social_button


def header() -> rx.Component:
    """
    This function returns the header component of the web application.
    :return:    The header component.
    """
    g = Gravatar("curto.brull.javier@gmail.com")
    color_border = color.Colors.PRIMARY.value
    image = g.get_image()
    return rx.flex(
        rx.card(
            rx.flex(
                rx.avatar(
                    src=image,
                    fallback="JCB",
                    size="8",
                    color_scheme="amber",
                    variant="solid",
                    radius="full",
                    margin_bottom=st.Sizes.DEFAULT.value,
                    border=f"5px solid {color_border}",
                ),
                rx.text(
                    "JAVIER CURTO",
                    size="5",
                    weight="bold",
                    color=color.Colors.WHITE.value,
                    align="center",
                    width=st.Percentages.FULL.value,
                    margin_bottom=st.Sizes.DEFAULT.value,
                ),
                rx.text(
                    "Desarrollador Backend",
                    style=st.text_card_subs,
                    align="center",
                ),
                rx.text(
                    "Java Spring",
                    style=st.text_card_subs,
                    align="center",
                ),
                rx.center(
                    rx.hstack(
                        link_social_button(
                            "linkedin.svg",
                            "https://www.linkedin.com/in/javier-curto-brull/",
                        ),
                        link_social_button(
                            "github.svg", "https://github.com/CurtoBrull"),
                        link_social_button(
                            "instagram.svg", "https://www.instagram.com/j.curtobrull/"
                        ),
                    ),
                    width=st.Percentages.FULL.value,
                ),
                flex_wrap="wrap",
                justify="center",
                align="center",
                width="180px",
            ),
            background_color=color.Colors.BG.value,
            size="3",
        ),
        id="header",
    )
