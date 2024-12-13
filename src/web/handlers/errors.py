"""Errors:
Este módulo contiene las Handlers Web para registrar y manejar errores hacia el Usuario final.

Clases:
----
- Error -- Representa un Error ocurrido.

Handlers:
----
- registrar_error_handlers -- Registra/Configura los handlers de Errores en la app Flask.
"""
from dataclasses import dataclass

from flask import Flask, render_template

_ERROR_TEMPLATE = "error.html"


@dataclass
class Error:
    """Representa un Error ocurrido en el sistema.

    Atributos:
    ----
    - code: int -- Código HTTP que representa el Error.
    - name: str -- Nombre del Error, visible al Usuario.
    - description: str -- Descripción largar o mensaje del Error, visible al Usuario.
    """
    code: int
    name: str
    description: str


def _not_found_error(e):
    """Handler para Error de tipo 404 'Not Found'.
    Sucede cuando no se encuentra un recurso solicitado por el Usuario.

    :return: Template renderizado del Error.
    :rtype: str
    """
    error = Error(404, "Recurso no encontrado", "El recurso solicitado no pudo ser encontrado.")
    return render_template(_ERROR_TEMPLATE, error=error), 404


def _unauthorized_error(e):
    """Handler para Error de tipo 401 'Unauthorized'.
    Sucede cuando se solicita de forma anónima un recurso que requiere autenticación.

    :return: Template renderizado del Error.
    :rtype: str
    """
    error = Error(401, "No autenticado", "El recuso u operación solicitado requiere autenticación.")
    return render_template(_ERROR_TEMPLATE, error=error), 401


def _forbidden_error(e):
    """Handler para Error de tipo 403 'Forbidden'.
    Sucede cuando se solicita un recurso sin contar con los permisos suficientes.

    :return: Template renderizado del Error.
    :rtype: str
    """
    error = Error(403, "No permitido", "Ud. no se encuentra autorizado a acceder al recurso u operación solicitado.")
    return render_template(_ERROR_TEMPLATE, error=error), 403


def registrar_error_handlers(app: Flask):
    """Registra todos los handlers de Errores para la app Flask dada.

    :param Flask app: App Flask donde configurar los handlers.
    """
    app.register_error_handler(404, _not_found_error)
    app.register_error_handler(401, _unauthorized_error)
    app.register_error_handler(403, _forbidden_error)
