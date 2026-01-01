def read_text(self):
    """
        Reads the content of a Word document and returns it as a string.
        :return: str, the content of the Word document.
        """
    try:
        doc = Document(self.file_path)
        full_text = []
        for paragraph in doc.paragraphs:
            full_text.append(paragraph.text)
        return '\n'.join(full_text)
    except:
        return ''