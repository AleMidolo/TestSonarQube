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
    merger = PyPDF2.PdfFileMerger()
    for reader in self.readers:
        merger.append(reader)
    merger.write(output_filepath)
    merger.close()
    return f'PDFs combinados guardados en {output_filepath}'