import reflex as rx
from reflex_web.components.navbar import navbar
from reflex_web.components.footer import footer
from reflex_web.views.header.header import header
from reflex_web.views.aboutme.aboutme import aboutme
from reflex_web.views.skills.skills import skills
from reflex_web.views.cv.cv import cv
from reflex_web.views.porfolio.portfolio import portfolio
from reflex_web.views.contact.contact import contact


class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        header(),
        aboutme(),
        skills(),
        cv(),
        portfolio(),
        contact(),
        footer()
    )


app = rx.App()
app.add_page(index)
