def add_rendition(self, lang, file_path):
    """Add a rendition (translation) of a document in a specific language.
    
    Args:
        lang (str): Language code for the rendition (e.g. 'en', 'es')
        file_path (str): Path to the rendition file
        
    Returns:
        dict: Updated renditions dictionary mapping language codes to file paths
    """
    if not hasattr(self, 'renditions'):
        self.renditions = {}
        
    if lang == 'original':
        self.renditions['originale'] = file_path
    else:
        self.renditions[lang] = file_path
        
    return self.renditions