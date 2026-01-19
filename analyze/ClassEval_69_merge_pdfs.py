def merge_pdfs(self, output_filepath):
    """
        Legge i file in self.readers che memorizza i riferimenti a più file PDF.
        Unisce questi file in un unico PDF e aggiorna il numero di pagina, quindi salva su disco.
        :param output_filepath: str, percorso del file di output in cui salvare
        :return: str, "PDF uniti salvati in {output_filepath}" se uniti con successo
        >>> handler = PDFHandler(['a.pdf', 'b.pdf'])
        >>> handler.merge_pdfs('out.pdf')
        PDF uniti salvati in out.pdf
        """
    if not self.readers:
        raise ValueError('No PDF files to merge')
    merger = PyPDF2.PdfMerger()
    for reader in self.readers:
        merger.append(reader)
    with open(output_filepath, 'wb') as output_file:
        merger.write(output_file)
    merger.close()
    return f'PDF uniti salvati in {output_filepath}'