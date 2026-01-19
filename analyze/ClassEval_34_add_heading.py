def add_heading(self, heading, level=1):
    """
    Agrega un encabezado al documento de Word.
    :param heading: str, el texto del encabezado.
    :param level: int, opcional, el nivel del encabezado (1, 2, 3, etc.; por defecto es 1).
    :return: bool, True si el encabezado se agrega correctamente, False en caso contrario.
    """
    try:
        if not isinstance(heading, str):
            return False
        if not isinstance(level, int) or level < 1:
            return False
        
        self.document.add_heading(heading, level=level)
        return True
    except Exception:
        return False