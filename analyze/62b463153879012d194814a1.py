def add_rendition(self, lang, file_path):
    """
    Adds a rendition of a file in a specified language.

    Args:
        lang (str): The language code for the rendition (e.g., 'en').
        file_path (str): The path to the rendition file.

    Example:
        {
            "original": "artigo02.pdf",
            "en": "artigo02-en.pdf",
        }
    """
    if not hasattr(self, 'renditions'):
        self.renditions = {}
    
    self.renditions[lang] = file_path