def add_rendition(self, lang, file_path):
    """
    Adds a rendition file path for a specific language to the renditions dictionary.
    
    Args:
        lang (str): Language code (e.g. 'en', 'es', etc). Use 'original' for the source file.
        file_path (str): Path to the rendition file
        
    Returns:
        None
        
    Example:
        {
            "original": "artigo02.pdf",
            "en": "artigo02-en.pdf",
        }
    """
    if not hasattr(self, 'renditions'):
        self.renditions = {}
    
    self.renditions[lang] = file_path