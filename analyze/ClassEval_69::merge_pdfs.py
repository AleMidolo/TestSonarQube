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
    merger = PyPDF2.PdfFileMerger()
    for reader in self.readers:
        merger.append(reader)
    merger.write(output_filepath)
    merger.close()
    return f'PDF uniti salvati in {output_filepath}'