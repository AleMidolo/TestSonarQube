def write_text(self, content, font_size=12, alignment='left'):
    """
    Escribe el contenido especificado en un documento de Word.
    :param content: str, el contenido de texto a escribir.
    :param font_size: int, opcional, el tamaño de fuente del texto (por defecto es 12).
    :param alignment: str, opcional, la alineación del texto ('left', 'center' o 'right'; por defecto es 'left').
    :return: bool, True si la operación de escritura es exitosa, False en caso contrario.
    """
    try:
        from docx import Document
        from docx.shared import Pt
        from docx.enum.text import WD_ALIGN_PARAGRAPH
        
        # Verificar que el documento existe o crear uno nuevo
        if not hasattr(self, 'document') or self.document is None:
            self.document = Document()
        
        # Agregar un párrafo con el contenido
        paragraph = self.document.add_paragraph(content)
        
        # Configurar el tamaño de fuente
        for run in paragraph.runs:
            run.font.size = Pt(font_size)
        
        # Configurar la alineación
        alignment_map = {
            'left': WD_ALIGN_PARAGRAPH.LEFT,
            'center': WD_ALIGN_PARAGRAPH.CENTER,
            'right': WD_ALIGN_PARAGRAPH.RIGHT
        }
        
        if alignment.lower() in alignment_map:
            paragraph.alignment = alignment_map[alignment.lower()]
        else:
            paragraph.alignment = WD_ALIGN_PARAGRAPH.LEFT
        
        return True
        
    except Exception as e:
        return False