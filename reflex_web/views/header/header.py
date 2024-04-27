"""
This module contains the header component for the web application.
It includes the avatar, name, role, skills, and social media links of the user.
"""

import reflex as rx
from libgravatar import Gravatar

from reflex_web.components.link_button import link_button


def header() -> rx.Component:
    """
    This function returns the header component of the web application.
    :return:    The header component.
    """
    g = Gravatar('curto.brull.javier@gmail.com')
    image = g.get_image()
    return rx.vstack(
        rx.box(
            rx.avatar(src=image,
                      fallback="JCB",
                      size="8",
                      color_scheme="amber",
                      variant="solid",
                      radius="full"),
            rx.text("JAVIER CURTO",
                    size="2",
                    weight="bold"),
            rx.text("Desarrollador Backend",
                    size="1",
                    color="gray"),
            rx.text("Java Spring",
                    size="1",
                    color="gray"),
            rx.hstack(
                link_button("LinkedIn", "https://www.linkedin.com/in/javier-curto-brull/"),
                link_button("Github", "https://github.com/CurtoBrull"),
                link_button("Instagram", "https://www.instagram.com/j.curtobrull/")
            )
        )
    )
