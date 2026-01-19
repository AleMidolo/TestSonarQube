def write_text(self, content, font_size=12, alignment='left'):
    """
    Writes the specified content to a Word document.
    :param content: str, the text content to write.
    :param font_size: int, optional, the font size of the text (default is 12).
    :param alignment: str, optional, the alignment of the text ('left', 'center', or 'right'; default is 'left').
    :return: bool, True if the write operation is successful, False otherwise.
    """
    try:
        from docx import Document
        from docx.shared import Pt
        from docx.enum.text import WD_ALIGN_PARAGRAPH
        
        # Check if document exists, otherwise create new one
        if not hasattr(self, 'document') or self.document is None:
            self.document = Document()
        
        # Add paragraph with content
        paragraph = self.document.add_paragraph(content)
        
        # Set font size
        for run in paragraph.runs:
            run.font.size = Pt(font_size)
        
        # Set alignment
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