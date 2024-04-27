import datetime as dt

import reflex as rx

from reflex_web.components.link_button import link_button


def footer() -> rx.Component:
    current_year = str(dt.datetime.now().year)
    url = "https://jcurto.eu"
    return rx.hstack(
        rx.text("\u24b8 2023-{} ".format(current_year),
                color="rgb(209, 150, 23)",
                font_size="1em"),
        rx.link(
            "Javier Curto Brull",
            href=url,
            color="rgb(209, 150, 23)",
            font_size="1.2em",
            font_weight="bold"
        ),
        link_button("LinkedIn", "https://www.linkedin.com/in/javier-curto-brull/"),
        link_button("Github", "https://github.com/CurtoBrull"),
        link_button("Instagram", "https://www.instagram.com/j.curtobrull/"),
        rx.image(src="favicon.ico", width=50, height=50, alt="favicon"),
        bg="#1e2326",
        padding_x="16px",
        padding_y="8px",
        width="100%",
        z_index="999",
    )
