def from_raw_values(cls, values):
    """
    Crear un objeto "Bookmarks" a partir de una lista de valores de marcadores en formato de cadena sin procesar.

    No deberías necesitar usar este método a menos que desees deserializar marcadores.

    :param values: Valores de cadenas ASCII (marcadores sin procesar)
    :type values: Iterable[str]
    """
    # Assuming the class "Bookmarks" has a constructor that accepts a list of processed values
    processed_values = [value.strip() for value in values]  # Example processing step
    return cls(processed_values)