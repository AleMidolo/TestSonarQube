def add_heading(self, heading, level=1):
    """
    Agrega un encabezado al documento de Word.
    :param heading: str, el texto del encabezado.
    :param level: int, opcional, el nivel del encabezado (1, 2, 3, etc.; por defecto es 1).
    :return: bool, True si el encabezado se agrega correctamente, False en caso contrario.
    """
    try:
        doc = Document(self.file_path)
        doc.add_heading(heading, level=level)
        doc.save(self.file_path)
        return True
    except:
        return False