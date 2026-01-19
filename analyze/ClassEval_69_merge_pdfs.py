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
    from PyPDF2 import PdfWriter
    
    writer = PdfWriter()
    
    # 遍历所有的 PDF readers，将每个页面添加到 writer 中
    for reader in self.readers:
        for page in reader.pages:
            writer.add_page(page)
    
    # 将合并后的 PDF 写入到输出文件
    with open(output_filepath, 'wb') as output_file:
        writer.write(output_file)
    
    return f"Merged PDFs saved at {output_filepath}"