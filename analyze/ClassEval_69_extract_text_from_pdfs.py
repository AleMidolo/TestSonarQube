def extract_text_from_pdfs(self):
    """
        Estrae il testo dai file pdf in self.readers
        :return pdf_texts: lista di str, ogni elemento è il testo di un file pdf
        >>> handler = PDFHandler(['a.pdf', 'b.pdf'])
        >>> handler.extract_text_from_pdfs()
        ['Test a.pdf', 'Test b.pdf']
        """
    pdf_texts = []
    for reader in self.readers:
        text = ''
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            page_text = page.extract_text()
            if page_text:
                text += page_text
        pdf_texts.append(text)
    return pdf_texts