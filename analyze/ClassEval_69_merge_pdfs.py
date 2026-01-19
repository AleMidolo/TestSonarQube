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
    from PyPDF2 import PdfWriter
    
    writer = PdfWriter()
    
    # Itera attraverso tutti i reader e aggiungi le loro pagine al writer
    for reader in self.readers:
        for page in reader.pages:
            writer.add_page(page)
    
    # Aggiorna il numero totale di pagine
    self.page_count = len(writer.pages)
    
    # Salva il PDF unito su disco
    with open(output_filepath, 'wb') as output_file:
        writer.write(output_file)
    
    return f"PDF uniti salvati in {output_filepath}"