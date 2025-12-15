def write_text(self, content, font_size=12, alignment='left'):
    """
    将指定的内容写入Word文档。
    :param content: str，要写入的文本内容。
    :param font_size: int，可选，文本的字体大小（默认为12）。
    :param alignment: str，可选，文本的对齐方式（'left'、'center'或'right'; 默认为'left'）。
    :return: bool，如果写入操作成功则返回True，否则返回False。
    """
    
    try:
        doc = Document(self.file_path)
        paragraph = doc.add_paragraph(content)
        run = paragraph.runs[0]
        run.font.size = Pt(font_size)
        paragraph.alignment = self._get_alignment_value(alignment)
        doc.save(self.file_path)
        return True
    except:
        return False