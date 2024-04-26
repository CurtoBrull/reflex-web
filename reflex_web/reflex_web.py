import reflex as rx


class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    return rx.avatar(src="../assets/favicon.ico")


app = rx.App()
app.add_page(index)
