def read_text(self):
    """
        Lee el contenido de un documento de Word y lo devuelve como una cadena.
        :return: str, el contenido del documento de Word.
        """
    try:
        doc = Document(self.file_path)
        full_text = []
        for paragraph in doc.paragraphs:
            full_text.append(paragraph.text)
        return '\n'.join(full_text)
    except:
        return ''