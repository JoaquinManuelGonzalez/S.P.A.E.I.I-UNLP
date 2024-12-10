"""Pagination:
Este módulo contiene las Handlers Web de las funcionalidades de paginación.

Handlers:
----
- query_pagination -- Parsea parámetros Query y retorna un número y tamaño de página solicitados.
"""
from werkzeug.datastructures.structures import MultiDict

_DEFAULT_PAGE = 1
_DEFAULT_PAGE_SIZE = 25


def query_pagination(query: MultiDict[str, str]) -> tuple[int, int]:
    """Obtiene parámetros comunes de un QueryString dado y retorna la solicitud de página correspondiente.
    En caso de no encontrarse los parámetros, se retorna una página de número y tamaño por defecto.

    :param MultiDict[str, str] query: QueryString a analizar.

    :return: Tuple con número y tamaño de página.
    :rtype: tuple[int, int]
    """
    try:
        page = int(query.get('page', _DEFAULT_PAGE))
    except ValueError:
        page = _DEFAULT_PAGE
    try:
        page_size = int(query.get('size', _DEFAULT_PAGE_SIZE))
    except ValueError:
        page_size = _DEFAULT_PAGE_SIZE
    return page, page_size
