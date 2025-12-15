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
        self.readers में फ़ाइलें पढ़ें जो कई PDF फ़ाइलों के हैंडल को संग्रहीत करती हैं।
        उन्हें एक PDF में मिलाएं और पृष्ठ संख्या को अपडेट करें, फिर डिस्क में सहेजें।
        :param output_filepath: str, सहेजने के लिए आउटपुट फ़ाइल पथ
        :return: str, "Merged PDFs saved at {output_filepath}" यदि सफलतापूर्वक मिलाया गया
        >>> handler = PDFHandler(['a.pdf', 'b.pdf'])
        >>> handler.merge_pdfs('out.pdf')
        Merged PDFs saved at out.pdf
        """
        merger = PyPDF2.PdfFileMerger()
        for reader in self.readers:
            merger.append(reader)
        merger.write(output_filepath)
        merger.close()
        return f"Merged PDFs saved at {output_filepath}"