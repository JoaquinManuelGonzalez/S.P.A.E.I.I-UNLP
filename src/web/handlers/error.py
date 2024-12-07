from flask import render_template
from dataclasses import dataclass

@dataclass
class Error:
    """
    Clase que representa un error.
    """
    code:int
    message:str
    description:str


def error_not_found(e):
    """
    Función que renderiza el template error.html con el error 404.

    Returns:
        render_template: Retorna el template error.html con el error 404.
    """
    error = Error(404, "Not Found","The requested URL was not found on the server")
    return render_template("error.html", error=error),error.code

def sin_permisos(e):
    """
    Función que renderiza el template error.html con el error 403.

    Returns:
        render_template: Retorna el template error.html con el error 403.
    """
    error = Error(403, "Forbidden","You don't have permission to access the requested resource")
    return render_template("error.html", error=error),error.code