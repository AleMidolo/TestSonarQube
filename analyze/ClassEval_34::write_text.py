def write_text(self, content, font_size=12, alignment='left'):
    """
    Escribe el contenido especificado en un documento de Word.
    :param content: str, el contenido de texto a escribir.
    :param font_size: int, opcional, el tamaño de fuente del texto (por defecto es 12).
    :param alignment: str, opcional, la alineación del texto ('left', 'center' o 'right'; por defecto es 'left').
    :return: bool, True si la operación de escritura es exitosa, False en caso contrario.
    """
    try:
        doc = Document(self.file_path)
        paragraph = doc.add_paragraph()
        run = paragraph.add_run(content)
        font = run.font
        font.size = Pt(font_size)
        alignment_value = self._get_alignment_value(alignment)
        paragraph.alignment = alignment_value
        doc.save(self.file_path)
        return True
    except Exception:
        return False