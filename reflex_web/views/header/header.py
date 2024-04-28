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
    return rx.box(
        rx.vstack(
            rx.avatar(src=image,
                      fallback="JCB",
                      size="8",
                      color_scheme="amber",
                      variant="solid",
                      radius="full"),
            rx.text("JAVIER CURTO",
                    size="5",
                    weight="bold",
                    color=st.Colors.WHITE),
            rx.text("Desarrollador Backend",
                    size="1",
                    color=st.Colors.WHITE),
            rx.text("Java Spring",
                    size="1",
                    color=st.Colors.WHITE),
            rx.hstack(
                link_button("Linkedin", "https://www.linkedin.com/in/javier-curto-brull/"),
                link_button("Github", "https://github.com/CurtoBrull"),
                link_button("Instagram", "https://www.instagram.com/j.curtobrull/")
            ),
            align="center",
            background_color=st.Colors.BG,
            padding=st.Spacing.SMALL,
            border_radius=st.Percentages.TENTH,
        ),
    )
