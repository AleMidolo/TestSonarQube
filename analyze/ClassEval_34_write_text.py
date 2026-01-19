def write_text(self, content, font_size=12, alignment='left'):
    """
        Scrive il contenuto specificato in un documento Word.
        :param content: str, il contenuto testuale da scrivere.
        :param font_size: int, opzionale, la dimensione del carattere del testo (predefinito è 12).
        :param alignment: str, opzionale, l'allineamento del testo ('left', 'center' o 'right'; predefinito è 'left').
        :return: bool, True se l'operazione di scrittura ha avuto successo, False altrimenti.
        """
    try:
        doc = Document(self.file_path)
        paragraph = doc.add_paragraph()
        run = paragraph.add_run(content)
        font = run.font
        font.size = Pt(font_size)
        paragraph.alignment = self._get_alignment_value(alignment)
        doc.save(self.file_path)
        return True
    except:
        return False