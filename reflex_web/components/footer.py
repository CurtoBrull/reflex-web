"""
This module contains the footer component for the web application.
It includes the current year, a link to website, and links profiles.
"""

import datetime as dt

import reflex as rx

import styles.styles as st
from reflex_web.components.link_button import link_button


def footer() -> rx.Component:
    """
    Footer component for the web application.
    :return: Component with the footer of the web application.
    """
    current_year = str(dt.datetime.now().year)
    url = "https://jcurto.eu"
    url_linkedin = "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9IiNmNDkzMGIiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBjbGFzcz0ibHVjaWRlIGx1Y2lkZS1hLWFycm93LWRvd24iPjxwYXRoIGQ9Ik0zLjUgMTNoNiIvPjxwYXRoIGQ9Im0yIDE2IDQuNS05IDQuNSA5Ii8+PHBhdGggZD0iTTE4IDd2OSIvPjxwYXRoIGQ9Im0xNCAxMiA0IDQgNC00Ii8+PC9zdmc+"

    return rx.hstack(
        rx.text(f"\u24b8 2023-{current_year} ",
                color=st.Colors.PRIMARY,
                font_size=st.Spacing.DEFAULT),
        rx.link(
            "Javier Curto Brull",
            href=url,
            color=st.Colors.SECONDARY,
            font_size="1.2em",
            font_weight="bold"
        ),
        link_button("Linkedin", "https://www.linkedin.com/in/javier-curto-brull/"),
        link_button("Github", "https://github.com/CurtoBrull"),
        link_button("Instagram", "https://www.instagram.com/j.curtobrull/"),
        rx.image(src="favicon.ico", width=50, height=50, alt="favicon"),
        bg=st.Colors.BG_SECONDARY,
        padding_x=st.Spacing.DEFAULT,
        padding_y=st.Spacing.SMALL,
        width=st.Percentages.FULL,
        position="sticky",
        bottom="0",
        z_index="999",
    )
