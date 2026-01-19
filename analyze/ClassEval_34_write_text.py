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
        
        # Validate inputs
        if not isinstance(content, str):
            return False
        
        if not isinstance(font_size, int) or font_size <= 0:
            return False
        
        # Add paragraph with content
        paragraph = self.add_paragraph(content)
        
        # Set font size
        run = paragraph.runs[0] if paragraph.runs else paragraph.add_run(content)
        run.font.size = docx.shared.Pt(font_size)
        
        # Set alignment
        alignment_map = {
            'left': WD_ALIGN_PARAGRAPH.LEFT,
            'center': WD_ALIGN_PARAGRAPH.CENTER,
            'right': WD_ALIGN_PARAGRAPH.RIGHT
        }
        
        if alignment.lower() not in alignment_map:
            return False
        
        paragraph.alignment = alignment_map[alignment.lower()]
        
        return True
        
    except Exception:
        return False