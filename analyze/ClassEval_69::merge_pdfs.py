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
        读取存储多个 PDF 文件句柄的 self.readers 中的文件。
        将它们合并为一个 PDF 并更新页码，然后保存到磁盘。
        :param output_filepath: str, 输出文件的保存路径
        :return: str, 如果成功合并则为"Merged PDFs saved at {output_filepath}" 
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