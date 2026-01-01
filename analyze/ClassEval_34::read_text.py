def read_text(self):
    """
        Lee el contenido de un documento de Word y lo devuelve como una cadena.
        :return: str, el contenido del documento de Word.
        """
    try:
        doc = Document(self.file_path)
        content = []
        for paragraph in doc.paragraphs:
            content.append(paragraph.text)
        return '\n'.join(content)
    except Exception as e:
        return str(e)