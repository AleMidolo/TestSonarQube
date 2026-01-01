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
    pdf_writer = PyPDF2.PdfFileWriter()
    for reader in self.readers:
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            pdf_writer.addPage(page)
    with open(output_filepath, 'wb') as output_file:
        pdf_writer.write(output_file)
    return f'Merged PDFs saved at {output_filepath}'