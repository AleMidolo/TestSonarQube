def add_asset(self, basename, file_path):
    """Adds an asset file path to the assets dictionary using the basename as key.
    
    Args:
        basename (str): Base filename to use as key
        file_path (str): Full file path to the asset
        
    Returns:
        dict: Updated assets dictionary
    """
    if not hasattr(self, 'assets'):
        self.assets = {}
        
    self.assets[basename] = file_path
    return self.assets