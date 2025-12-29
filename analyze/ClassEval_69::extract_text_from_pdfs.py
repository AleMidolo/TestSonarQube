def extract_text_from_pdfs(self):
    """
        Extract text from pdf files in self.readers
        :return pdf_texts: list of str, each element is the text of one pdf file
        >>> handler = PDFHandler(['a.pdf', 'b.pdf'])
        >>> handler.extract_text_from_pdfs()
        ['Test a.pdf', 'Test b.pdf']
        """
    pdf_texts = []
    for reader in self.readers:
        text = ''
        for page in reader.pages:
            text += page.extract_text() or ''
        pdf_texts.append(text)
    return pdf_texts