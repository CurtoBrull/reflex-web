"""
This module contains the contact component for the web application.
Currently, it only returns a text component with the string "Contacto".
"""

import reflex as rx


def contact() -> rx.Component:
    """
        This function returns a component "Contact".
        :return rx.Component: "Contacto".
        """
    return rx.text("Contacto")
