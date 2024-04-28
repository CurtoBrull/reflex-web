"""
This module contains the header component for the web application.
It includes the avatar, name, role, skills, and social media links of the user.
"""

import reflex as rx
from libgravatar import Gravatar

import styles.styles as st
from reflex_web.components.link_button import link_button


def header() -> rx.Component:
    """
    This function returns the header component of the web application.
    :return:    The header component.
    """
    g = Gravatar('curto.brull.javier@gmail.com')
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
                    margin_bottom=st.Spacing.DEFAULT
                ),
                rx.text(
                    "JAVIER CURTO",
                    size="5",
                    weight="bold",
                    color=st.Colors.WHITE,
                    align="center",
                    width=st.Percentages.FULL,
                    margin_bottom=st.Spacing.DEFAULT
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
                        link_button(
                            "Linkedin",
                            "https://www.linkedin.com/in/javier-curto-brull/"
                        ),
                        link_button(
                            "Github",
                            "https://github.com/CurtoBrull"
                        ),
                        link_button(
                            "Instagram",
                            "https://www.instagram.com/j.curtobrull/"
                        )
                    ),
                    width=st.Percentages.FULL
                ),
                flex_wrap="wrap",
                justify="center",
                align="center",
                width="180px",
            ),
            background_color=st.Colors.BG,
            size="3"
        ),
    )
