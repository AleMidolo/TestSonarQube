def from_raw_values(cls, values):
    """
    Crear un objeto "Bookmarks" a partir de una lista de valores de marcadores en formato de cadena sin procesar.

    No deberías necesitar usar este método a menos que desees deserializar marcadores.

    :param values: Valores de cadenas ASCII (marcadores sin procesar)
    :type values: Iterable[str]
    """
    # Assuming the Bookmarks class is defined elsewhere and has a method to add bookmarks
    bookmarks = cls()
    for value in values:
        # Process each raw value and add it to the Bookmarks object
        bookmarks.add_bookmark(value)
    return bookmarks