def _validate_name(self, name: str) -> str:
    """
    Valida el nombre y lo devuelve. Si el nombre está vacío o excede los 33 caracteres de longitud, se establece en None.
    :param name: str, el nombre a validar
    :return: str, el nombre validado o None si es inválido
    """
    if not name or len(name) > 33:
        return None
    return name