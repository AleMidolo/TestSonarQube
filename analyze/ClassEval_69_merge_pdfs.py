def merge_pdfs(self, output_filepath):
    """
        Lee archivos en self.readers que almacena manejadores a múltiples archivos PDF.
        Los combina en un solo PDF y actualiza el número de página, luego lo guarda en disco.
        :param output_filepath: str, ruta del archivo de salida para guardar
        :return: str, "PDFs combinados guardados en {output_filepath}" si se combinó con éxito
        >>> handler = PDFHandler(['a.pdf', 'b.pdf'])
        >>> handler.merge_pdfs('out.pdf')
        PDFs combinados guardados en out.pdf
        """
    pdf_writer = PyPDF2.PdfFileWriter()
    for reader in self.readers:
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            pdf_writer.add_page(page)
    with open(output_filepath, 'wb') as out_file:
        pdf_writer.write(out_file)
    return f'PDFs combinados guardados en {output_filepath}'