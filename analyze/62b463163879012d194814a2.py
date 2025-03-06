def add_asset(self, basename, file_path):
    """
    Adds an asset to the dictionary with the given basename and file path.
    
    Args:
        basename (str): The base name of the asset.
        file_path (str): The full path to the asset file.
    
    Returns:
        None
    """
    if not hasattr(self, 'assets'):
        self.assets = {}
    
    self.assets[basename] = file_path