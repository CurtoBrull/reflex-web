"""
This module contains the cv component for the web application.
Currently, it only returns a text component with the string "Currículum".
"""

import reflex as rx


def cv() -> rx.Component:
    """
            This function returns a component "CV".
            :return Component: "Currículum".
            """
    return rx.text("Currículum")
