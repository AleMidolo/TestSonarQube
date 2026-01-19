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
    return f'Merged PDFs saved at {output_filepath}'