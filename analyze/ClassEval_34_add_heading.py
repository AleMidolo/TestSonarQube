def add_heading(self, heading, level=1):
    """
    向Word文档添加标题。
    :param heading: str，标题的文本。
    :param level: int，可选，标题的级别（1, 2, 3等；默认为1）。
    :return: bool，如果标题成功添加则返回True，否则返回False。
    """
    try:
        if not isinstance(heading, str):
            return False
        
        if not isinstance(level, int) or level < 1:
            return False
        
        # Assuming this is part of a class that uses python-docx
        # and self.document is a Document object
        if hasattr(self, 'document'):
            self.document.add_heading(heading, level=level)
            return True
        else:
            return False
    except Exception as e:
        return False