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
    from PyPDF2 import PdfMerger
    
    merger = PdfMerger()
    
    for reader in self.readers:
        merger.append(reader)
    
    merger.write(output_filepath)
    merger.close()
    
    return f"Merged PDFs saved at {output_filepath}"