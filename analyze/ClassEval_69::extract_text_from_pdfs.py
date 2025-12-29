def extract_text_from_pdfs(self):
    """
        从 self.readers 中的 pdf 文件提取文本
        :return pdf_texts: str 列表，每个元素是一个 pdf 文件的文本
        >>> handler = PDFHandler(['a.pdf', 'b.pdf'])
        >>> handler.extract_text_from_pdfs()
        ['Test a.pdf', 'Test b.pdf']
        """
    pdf_texts = []
    for reader in self.readers:
        text = ''
        for page in reader.pages:
            text += page.extract_text()
        pdf_texts.append(text)
    return pdf_texts