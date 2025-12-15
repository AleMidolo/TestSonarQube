def read_text(self):
        """
        Legge il contenuto di un documento Word e lo restituisce come stringa.
        :return: str, il contenuto del documento Word.
        """
        try:
            doc = Document(self.file_path)
            content = []
            for paragraph in doc.paragraphs:
                content.append(paragraph.text)
            return '\n'.join(content)
        except Exception as e:
            return str(e)