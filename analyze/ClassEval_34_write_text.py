def write_text(self, content, font_size=12, alignment='left'):
    """
    Scrive il contenuto specificato in un documento Word.
    :param content: str, il contenuto testuale da scrivere.
    :param font_size: int, opzionale, la dimensione del carattere del testo (predefinito è 12).
    :param alignment: str, opzionale, l'allineamento del testo ('left', 'center' o 'right'; predefinito è 'left').
    :return: bool, True se l'operazione di scrittura ha avuto successo, False altrimenti.
    """
    try:
        from docx.enum.text import WD_ALIGN_PARAGRAPH
        
        # Aggiungi un paragrafo con il contenuto
        paragraph = self.document.add_paragraph(content)
        
        # Imposta la dimensione del carattere
        for run in paragraph.runs:
            run.font.size = docx.shared.Pt(font_size)
        
        # Se il paragrafo è vuoto (nessun run), aggiungi il testo
        if not paragraph.runs:
            run = paragraph.add_run(content)
            run.font.size = docx.shared.Pt(font_size)
        
        # Imposta l'allineamento
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