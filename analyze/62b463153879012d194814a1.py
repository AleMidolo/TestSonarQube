def add_rendition(self, lang, file_path):
    """Add a new rendition of the document in a specific language.
    
    Args:
        lang (str): The language code for the rendition (e.g., 'en' for English).
        file_path (str): The file path to the rendition document.
    """
    if not hasattr(self, 'renditions'):
        self.renditions = {}
    self.renditions[lang] = file_path