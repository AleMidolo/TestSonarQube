def read_text(self):
    """
        Legge il contenuto di un documento Word e lo restituisce come stringa.
        :return: str, il contenuto del documento Word.
        """
    try:
        doc = Document(self.file_path)
        full_text = []
        for paragraph in doc.paragraphs:
            full_text.append(paragraph.text)
        return '\n'.join(full_text)
    except:
        return ''