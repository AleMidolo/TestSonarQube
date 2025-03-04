def from_raw_values(cls, values):
    """
    Crear un objeto "Bookmarks" a partir de una lista de valores de marcadores en formato de cadena sin procesar.

    No deberías necesitar usar este método a menos que desees deserializar marcadores.

    :param values: Valores de cadenas ASCII (marcadores sin procesar)
    :type values: Iterable[str]
    """
    bookmarks = []
    for value in values:
        try:
            # Remove any whitespace and validate string is not empty
            bookmark = value.strip()
            if bookmark:
                bookmarks.append(bookmark)
        except (AttributeError, TypeError):
            # Skip invalid values that can't be converted to string
            continue
            
    return cls(bookmarks)