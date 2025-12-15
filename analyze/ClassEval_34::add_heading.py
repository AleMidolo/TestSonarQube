def add_heading(self, heading, level=1):
    """
    Adds a heading to the Word document.
    :param heading: str, the text of the heading.
    :param level: int, optional, the level of the heading (1, 2, 3, etc.; default is 1).
    :return: bool, True if the heading is successfully added, False otherwise.
    """
    
    try:
        doc = Document(self.file_path)
        doc.add_heading(heading, level=level)
        doc.save(self.file_path)
        return True
    except:
        return False