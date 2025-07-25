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
            # Remove any whitespace and validate string
            value = value.strip()
            if value:
                # Convert string to float if possible
                bookmark = float(value)
                bookmarks.append(bookmark)
        except ValueError:
            # Skip invalid values
            continue
            
    return cls(bookmarks)