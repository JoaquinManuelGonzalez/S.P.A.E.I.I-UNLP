from wtforms.validators import ValidationError
import re

def file_size_limit(max_size_in_mb):
    """
    Validador que limita el tamaño de un archivo a subir.
    """
    max_bytes = max_size_in_mb * 1024 * 1024

    def _file_size_limit(form, field):
        if field.data:
            file_size = len(field.data.read())
            field.data.seek(0)
            if file_size > max_bytes:
                raise ValidationError(
                    f"El archivo no debe superar los {max_size_in_mb} MB."
                )

    return _file_size_limit


def solo_letras(cadena) -> bool:
    """
    Verifica si una cadena sólo contiene letras
    Args:
        cadena:
            Cadena a chequear si es válida.

    Returns:
        bool:
            True si la cadena son sólo letras, False si no.
    """
    return bool(re.fullmatch(r"^[a-zA-Z\s]+$", cadena))


def solo_numeros(cadena) -> bool:
    """
    Verifica si una cadena solo contiene dígitos numéricos.
    Args:
        cadena:
            Cadena a chequear si es válida.

    Returns:
        bool:
            True si la cadena son sólo números, False si no.
    """
    return bool(re.fullmatch(r"^[0-9]+$", cadena))


def solo_fechas(cadena) -> bool:
    """
    Verificar si la cadena es una fecha.
    Args:
        cadena:
            Cadena a chequear si es válida.

    Returns:
        bool:
            True si la cadena es una fecha válida, False si no.
    """
    return bool(re.fullmatch(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", cadena))


def es_correo_valido(correo) -> bool:
    """
    Verifica si una cadena es un correo electrónico válido y no está vacía.
    Args:
        correo:
            Cadena a chequear si es válida.

    Returns:
        bool:
            True si la cadena es un correo electrónico válido y no está vacía, False si no.
    """
    return bool(
        re.fullmatch(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", correo)
    )


def letras_y_numeros(cadena) -> bool:
    """
    Verifica si una cadena no está vacía y es válida.
    Una cadena válida puede tener letras, números y espacios.
    Args:
        cadena:
            Cadena a chequear si es válida.

    Returns:
        bool:
            True si la cadena no está vacía y es válida, False si no.
    """
    return bool(re.fullmatch(r"^[a-zA-Z0-9\s]+$", cadena))


def es_enlace_valido(enlace) -> bool:
    """
    Verifica si una cadena es un enlace (URL) válido.
    Args:
        enlace:
            Cadena a chequear si es válida.

    Returns:
        bool:
            True si la cadena es un enlace válido, False si no.
    """
    regex = re.compile(
        r"^(https?|ftp):\/\/"
        r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"
        r"localhost|"
        r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|"
        r"\[?[A-F0-9]*:[A-F0-9:]+\]?)"
        r"(?::\d+)?"
        r"(?:\/[^\s]*)?$",
        re.IGNORECASE,
    )
    return re.match(regex, enlace) is not None


def texto_con_signos(cadena) -> bool:
    """
    Verifica si una cadena es válida.
    Una cadena válida puede tener letras (incluyendo tildes), números, espacios y signos de puntuación.
    Args:
        cadena:
            Cadena a chequear si es válida.

    Returns:
        bool:
            True si la cadena es válida, False si no.
    """
    return bool(re.fullmatch(r"^[a-zA-Z0-9\s,!?;:.@#&()\"'%-áéíóúÁÉÍÓÚñÑ]+$", cadena))


def solo_letras_caracteres(cadena) -> bool:
    # Verificar si solo contiene letras y guiones bajos
    return bool(re.fullmatch(r"^[a-zA-Z\s_]+$", cadena))


def formulario_valido(form_data, validation_rules):
    """
    Validador que verifica si el formulario es válido.
    Chequea que no haya campos vacíos y que no haya errores de validación según el campo.
    Args:
        form_data:
            Formulario a ser validado.
        validation_rules:
            Reglas de validación para los campos del formulario.

    Returns:
        bool, dict:
            True si el formulario es válido. False si no.
            Diccionario con los errores.
    """
    errors = {}
    validation_messages = {
        solo_letras: "Este campo solo puede contener letras.",
        solo_numeros: "Este campo solo puede contener números.",
        solo_fechas: "Este campo debe tener el formato YYYY-MM-DD.",
        letras_y_numeros: "Este campo solo puede contener letras, números y espacios.",
        es_correo_valido: "Este campo debe ser un correo electrónico válido.",
        es_enlace_valido: "Este campo debe ser un enlace válido.",
        contacto_estado_valido: "Este campo debe ser 'pendiente', 'atendido','cancelado', 'rechazado', 'en proceso', 'completado'.",
        contacto_comentario_valido: "Este campo solo puede contener letras, números y espacios.",
    }

    for field_name, field_value in form_data.items():
        if field_name in validation_rules:
            if not field_value:
                errors[field_name] = ["Este campo no puede estar vacío."]
                return False, errors
            validation_func = validation_rules[field_name]
            if not validation_func(field_value):
                errors[field_name] = [
                    validation_messages.get(validation_func, "Error de validación.")
                ]
                return False, errors

    return True, errors
