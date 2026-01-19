def merge_pdfs(self, output_filepath):
    """
        Read files in self.readers which stores handles to multiple PDF files.
        Merge them to one pdf and update the page number, then save in disk.
        :param output_filepath: str, ouput file path to save to
        :return: str, "Merged PDFs saved at {output_filepath}" if successfully merged
        >>> handler = PDFHandler(['a.pdf', 'b.pdf'])
        >>> handler.merge_pdfs('out.pdf')
        Merged PDFs saved at out.pdf
        """
    pdf_writer = PyPDF2.PdfFileWriter()
    for reader in self.readers:
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            pdf_writer.addPage(page)
    with open(output_filepath, 'wb') as output_file:
        pdf_writer.write(output_file)
    return f'Merged PDFs saved at {output_filepath}'