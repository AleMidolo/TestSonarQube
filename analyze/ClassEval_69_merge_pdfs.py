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
    from PyPDF2 import PdfWriter, PdfReader
    
    writer = PdfWriter()
    
    # सभी PDF readers से पृष्ठों को मिलाएं
    for reader in self.readers:
        for page in reader.pages:
            writer.add_page(page)
    
    # मर्ज की गई PDF को डिस्क में सहेजें
    with open(output_filepath, 'wb') as output_file:
        writer.write(output_file)
    
    return f"Merged PDFs saved at {output_filepath}"