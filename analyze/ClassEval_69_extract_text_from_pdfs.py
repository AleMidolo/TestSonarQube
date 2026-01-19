def extract_text_from_pdfs(self):
    """
    self.readers में pdf फ़ाइलों से पाठ निकालें
    :return pdf_texts: str की सूची, प्रत्येक तत्व एक pdf फ़ाइल के पाठ है
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