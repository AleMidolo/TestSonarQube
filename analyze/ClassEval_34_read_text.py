def read_text(self):
    """
    读取Word文档的内容并将其作为字符串返回。
    :return: str,Word文档的内容。
    """
    from docx import Document
    
    doc = Document(self.file_path)
    full_text = []
    
    for paragraph in doc.paragraphs:
        full_text.append(paragraph.text)
    
    return '\n'.join(full_text)