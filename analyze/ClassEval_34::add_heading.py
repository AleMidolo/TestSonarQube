def add_heading(self, heading, level=1):
    """
        向Word文档添加标题。
        :param heading: str，标题的文本。
        :param level: int，可选，标题的级别（1, 2, 3等；默认为1）。
        :return: bool，如果标题成功添加则返回True，否则返回False。
        """
    try:
        doc = Document(self.file_path)
        doc.add_heading(heading, level=level)
        doc.save(self.file_path)
        return True
    except:
        return False