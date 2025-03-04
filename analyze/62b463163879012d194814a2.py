def add_asset(self, basename, file_path):
    """Adds an asset file path mapping to the assets dictionary.
    
    Args:
        basename (str): The base filename without path
        file_path (str): The full file path to the asset
        
    Returns:
        dict: Updated assets dictionary with new basename:file_path mapping
    """
    if not hasattr(self, 'assets'):
        self.assets = {}
        
    self.assets[basename] = file_path
    return self.assets