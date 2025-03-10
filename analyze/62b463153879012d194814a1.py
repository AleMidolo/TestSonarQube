def add_rendition(self, lang, file_path):
    """
    Adds a new rendition to the document's rendition dictionary.

    Args:
        lang (str): The language code for the rendition (e.g., 'en' for English).
        file_path (str): The file path of the rendition.

    Returns:
        None
    """
    if not hasattr(self, 'renditions'):
        self.renditions = {}
    self.renditions[lang] = file_path