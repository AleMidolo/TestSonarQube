def add_rendition(self, lang, file_path):
    """Add a rendition (translation) of a file for a specific language.
    
    Args:
        lang (str): Language code for the rendition (e.g. 'en', 'es')
        file_path (str): Path to the rendition file
        
    Returns:
        dict: Dictionary mapping language codes to file paths
    """
    if not hasattr(self, '_renditions'):
        self._renditions = {}
        
    if lang == 'original':
        self._renditions['originale'] = file_path
    else:
        self._renditions[lang] = file_path
        
    return self._renditions