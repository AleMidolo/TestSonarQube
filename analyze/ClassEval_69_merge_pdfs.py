def __init__(self, pdf_files):
    """
    初始化 PDFHandler
    :param pdf_files: list of str, PDF 文件路径列表
    """
    self.pdf_files = pdf_files
    self.readers = [PdfReader(pdf_file) for pdf_file in pdf_files]