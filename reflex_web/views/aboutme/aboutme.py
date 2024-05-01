"""
This module contains the aboutme component for the web application.
Currently, it only returns a text component with the string "Sobre Mí".
"""

import reflex as rx

import styles.styles as st
import styles.colors as color


def aboutme() -> rx.Component:
    """
    Returns a text component with the string "Sobre Mí".
    :return: Component "Sobre Mí".
    """
    return rx.box(
        rx.center(
            rx.text(
                "Sobre Mí",
                style=st.text_h1_title_style
            ),
        ),
        rx.vstack(
            rx.text(
                "¡Hola! Soy Javier Curto.",
                style=st.text_h2_style,
            ),
            rx.text("Decidido dar el paso fuera de mi zona de confort, "
                    "finalmente me embarqué en el fascinante viaje de explorar mi pasión por la informática y la "
                    "programación. "
                    "Comencé mi formación con el CFGM de Sistemas Microinformáticos y Redes, "
                    "y luego continué con el CFGS de Desarrollo de Aplicaciones Web, "
                    "adentrándome en un mundo apasionante y en constante evolución."),
            rx.text("Actualmente, cuento con conocimientos en una variedad de tecnologías, "
                    "incluyendo Java, Spring, HTML, CSS, JavaScript, PHP y JQuery, entre otras. "
                    "Sin embargo, mi sed de aprendizaje continúa, y estoy siempre en búsqueda de nuevas habilidades y "
                    "conocimientos."),
            rx.text("Mi rol actual como Desarrollador Backend con Java Spring en NTT Data, "
                    "me permite seguir creciendo y perfeccionándome día a día. "
                    "Actualmente, estoy inmerso en un proyecto para una importante empresa textil, "
                    "donde gestionamos el almacenamiento en bases de datos, tales como DB2 y MongoDB, "
                    "de los movimientos de stock en sus tiendas. Este desafío me permite aplicar mis habilidades "
                    "y conocimientos en un entorno dinámico y exigente, "
                    "contribuyendo a un proyecto crucial para nuestro cliente."),
        ),
        rx.hstack(
            rx.box(
                rx.text(
                    "Datos Personales",
                    style=st.text_h3_style
                ),
                rx.list(
                    rx.list.item("Email"),
                    rx.list.item("curto.brull.javier@jcurto.eu"),
                    rx.list.item("Vivo en"),
                    rx.list.item("Huércal de Almería"),
                ),
                width=st.Percentages.HALF.value,

            ),
            rx.box(
                rx.text(
                    "Intereses",
                    style=st.text_h3_style
                ),
                rx.list(
                    rx.list.item("Example 1"),
                    rx.list.item("Example 2"),
                    rx.list.item("Example 3"),
                ),
                width=st.Percentages.HALF.value
            ),
            margin=st.Sizes.DEFAULT.value,
        ),
        id="aboutme",
        padding=st.Sizes.DEFAULT.value,
        bg=color.Colors.BG.value
    )
