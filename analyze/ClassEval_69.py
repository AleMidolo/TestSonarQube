import PyPDF2


class PDFHandler:
    def __init__(self, filepaths):
        self.filepaths = filepaths
        self.readers = self._initialize_readers(filepaths)

    def _initialize_readers(self, filepaths):
        return [PyPDF2.PdfReader(fp) for fp in filepaths]

    def merge_pdfs(self, output_filepath):
        pdf_writer = PyPDF2.PdfWriter()
        self._add_pages_to_writer(pdf_writer)
        self._write_pdf(pdf_writer, output_filepath)
        return f"Merged PDFs saved at {output_filepath}"

    def _add_pages_to_writer(self, pdf_writer):
        for reader in self.readers:
            for page in reader.pages:
                pdf_writer.add_page(page)

    def _write_pdf(self, pdf_writer, output_filepath):
        with open(output_filepath, 'wb') as out:
            pdf_writer.write(out)

    def extract_text_from_pdfs(self):
        return [self._extract_text_from_reader(reader) for reader in self.readers]

    def _extract_text_from_reader(self, reader):
        return [page.extract_text() for page in reader.pages]