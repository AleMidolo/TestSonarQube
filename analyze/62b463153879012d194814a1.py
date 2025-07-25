def add_rendition(self, lang, file_path):
    """Adds a rendition file for a specific language to the document.
    
    Args:
        lang (str): Language code for the rendition (e.g. 'en', 'es')
        file_path (str): Path to the rendition file
        
    Returns:
        dict: Updated renditions dictionary mapping languages to file paths
    """
    if not hasattr(self, 'renditions'):
        self.renditions = {}
        
    if lang == 'original':
        self.renditions['originale'] = file_path
    else:
        self.renditions[lang] = file_path
        
    return self.renditions