import reflex as rx
from reflex_web.components.link_button import link_button


def footer() -> rx.Component:
    return rx.hstack(
        link_button("LinkedIn", "https://www.linkedin.com/in/javier-curto-brull/"),
        link_button("Github", "https://github.com/CurtoBrull"),
        link_button("Instagram", "https://www.instagram.com/j.curtobrull/"),
    )
