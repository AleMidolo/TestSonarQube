def add_rendition(self, lang, file_path):
    """
    Adds a new rendition of the document in the specified language.

    Args:
        lang (str): The language code for the rendition (e.g., 'en' for English).
        file_path (str): The file path to the rendition document.

    Returns:
        None
    """
    if not hasattr(self, 'renditions'):
        self.renditions = {}
    
    self.renditions[lang] = file_path