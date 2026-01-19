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
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        pdf_texts.append(text)
    
    return pdf_texts