import PyPDF2

class PDFHandler: 
    def __init__(self, filepaths):
        """
        takes a list of file paths filepaths as a parameter.
        It creates a list named readers using PyPDF2, where each reader opens a file from the given paths.
        """
        self.filepaths = filepaths
        self.readers = [PyPDF2.PdfFileReader(fp) for fp in filepaths]

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
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                pdf_texts.append(page.extract_text())
        return pdf_texts
    
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
        pdf_writer = PyPDF2.PdfFileWriter()
        for reader in self.readers:
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                pdf_writer.add_page(page)
        
        with open(output_filepath, 'wb') as out_file:
            pdf_writer.write(out_file)
        
        return f"PDF uniti salvati in {output_filepath}"