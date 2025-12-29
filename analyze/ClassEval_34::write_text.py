def write_text(self, content, font_size=12, alignment='left'):
    """
        Writes the specified content to a Word document.
        :param content: str, the text content to write.
        :param font_size: int, optional, the font size of the text (default is 12).
        :param alignment: str, optional, the alignment of the text ('left', 'center', or 'right'; default is 'left').
        :return: bool, True if the write operation is successful, False otherwise.
        """
    try:
        doc = Document(self.file_path)
        paragraph = doc.add_paragraph(content)
        paragraph.alignment = self._get_alignment_value(alignment)
        for run in paragraph.runs:
            run.font.size = Pt(font_size)
        doc.save(self.file_path)
        return True
    except Exception:
        return False