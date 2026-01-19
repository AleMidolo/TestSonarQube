def add_heading(self, heading, level=1):
    """
    Adds a heading to the Word document.
    :param heading: str, the text of the heading.
    :param level: int, optional, the level of the heading (1, 2, 3, etc.; default is 1).
    :return: bool, True if the heading is successfully added, False otherwise.
    """
    try:
        if not isinstance(heading, str):
            return False
        if not isinstance(level, int) or level < 1:
            return False
        
        # Assuming this is a method of a class that has a document object
        # Using python-docx library convention
        self.document.add_heading(heading, level=level)
        return True
    except Exception:
        return False