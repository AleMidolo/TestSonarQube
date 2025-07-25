def add_asset(self, basename, file_path):
    """
    Adds an asset file to the assets dictionary.
    
    Args:
        basename (str): Base name of the asset file
        file_path (str): Full file path to the asset
        
    Returns:
        dict: Updated assets dictionary with new asset added
    """
    if not hasattr(self, 'assets'):
        self.assets = {}
        
    self.assets[basename] = file_path
    return self.assets