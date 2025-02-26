def add_rendition(self, lang, file_path):
    """
    Adds a rendition of the original file in the specified language.

    Args:
        lang (str): The language code for the rendition (e.g., 'en').
        file_path (str): The file path of the rendition to be added.

    Example:
        {
            "original": "artigo02.pdf",
            "en": "artigo02-en.pdf",
        }
    """
    if not hasattr(self, 'renditions'):
        self.renditions = {}
    
    self.renditions[lang] = file_path