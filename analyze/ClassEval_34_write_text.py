def write_text(self, content, font_size=12, alignment='left'):
    """
    Escribe el contenido especificado en un documento de Word.
    :param content: str, el contenido de texto a escribir.
    :param font_size: int, opcional, el tamaño de fuente del texto (por defecto es 12).
    :param alignment: str, opcional, la alineación del texto ('left', 'center' o 'right'; por defecto es 'left').
    :return: bool, True si la operación de escritura es exitosa, False en caso contrario.
    """
    try:
        from docx.enum.text import WD_ALIGN_PARAGRAPH
        
        # Validar parámetros
        if not isinstance(content, str):
            return False
        
        if not isinstance(font_size, int) or font_size <= 0:
            return False
        
        # Mapeo de alineación
        alignment_map = {
            'left': WD_ALIGN_PARAGRAPH.LEFT,
            'center': WD_ALIGN_PARAGRAPH.CENTER,
            'right': WD_ALIGN_PARAGRAPH.RIGHT
        }
        
        if alignment.lower() not in alignment_map:
            return False
        
        # Agregar párrafo al documento
        paragraph = self.add_paragraph(content)
        
        # Configurar tamaño de fuente
        for run in paragraph.runs:
            run.font.size = docx.shared.Pt(font_size)
        
        # Configurar alineación
        paragraph.alignment = alignment_map[alignment.lower()]
        
        return True
        
    except Exception as e:
        return False