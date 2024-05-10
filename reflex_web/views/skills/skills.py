"""
This module contains the skills component for the web application.
Currently, it only returns a text component with the string "Skills".
"""

import reflex as rx

import styles.styles as st
import styles.colors as color
from reflex_web.components.skills_text import skills_list_item

CFGS = "Conocimientos del lenguaje gracias al ciclo formativo de Desarrollo de Aplicaciones Web."


def skills() -> rx.Component:
    """
    Returns a text component with the string "Skills".
    :return: Component "Skills"
    """
    return rx.box(
        rx.center(
            rx.text(
                "Skills",
                style=st.text_h1_title_style,
            ),
            bg=color.Colors.BG_SECONDARY.value,
        ),
        rx.flex(
            rx.box(
                rx.text(
                    "Technical Skills",
                    style=st.text_h2_title_style,
                    text_align="center",
                ),
                skills_list_item("Java", "Mi lenguaje del día a día."),
                skills_list_item(
                    "Spring", "Experiencia real en proyectos con este Framework de desarrollo de aplicaciones Java."),
                skills_list_item(
                    "Git y Github", "Manejo de bases de datos relacionales."),
                skills_list_item(
                    "SQL", "Manejo de bases de datos relacionales."),
                skills_list_item(
                    "DB2", "Manejo de bases de datos relacionales en proyectos reales."),
                skills_list_item(
                    "MongoDB", "Manejo de bases de datos NoSQL en proyectos reales."),
                skills_list_item("Postman", "Pruebas de API REST."),
                skills_list_item(
                    "Python", "Conocimientos del lenguaje, esta web está hecha con Reflex y Python puro."),
                skills_list_item(
                    "HTML & CSS", "Conocimientos en los fundamentos del diseño web."),
                skills_list_item("Javascript", CFGS),
                skills_list_item("PHP", CFGS),
                skills_list_item("JQuery", CFGS),
            ),
            rx.box(
                rx.text(
                    "Professional Skills",
                    style=st.text_h2_title_style,
                    text_align="center",
                ),
                skills_list_item("Trabajo en equipo",
                                 "Experiencia en proyectos en equipo."),
                skills_list_item(
                    "Comunicación", "Habilidad para transmitir ideas de manera efectiva."),
                skills_list_item(
                    "Adaptabilidad", "Capacidad para adaptarme a diferentes situaciones."),
                skills_list_item(
                    "Dedicación", "Compromiso con los proyectos en los que participo."),
                skills_list_item("Gestión del tiempo",
                                 "Organización eficiente del tiempo."),
                skills_list_item(
                    "Autoaprendizaje", "Capacidad para aprender de manera autónoma."),
                skills_list_item(
                    "Desarrollo Ágil", "Experiencia en proyectos con metodologías ágiles como SCRUM."),
                margin_left=st.Sizes.SMALL.value,
            ),
            margin=st.Sizes.BIG.value,
            justify="between",
            wrap="wrap",
            direction="row",
            justify_content="center"
        ),
        bg=color.Colors.BG_SECONDARY.value,
    )
