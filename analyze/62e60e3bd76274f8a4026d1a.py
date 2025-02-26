def from_raw_values(cls, values):
    """
    Crear un objeto "Bookmarks" a partir de una lista de valores de marcadores en formato de cadena sin procesar.

    No deberías necesitar usar este método a menos que desees deserializar marcadores.

    :param values: Valores de cadenas ASCII (marcadores sin procesar)
    :type values: Iterable[str]
    """
    bookmarks = []
    for value in values:
        # Suponiendo que cada valor es una cadena que representa un marcador
        # Aquí se puede agregar lógica para procesar cada valor según sea necesario
        bookmarks.append(value.strip())  # Eliminar espacios en blanco
    return cls(bookmarks)