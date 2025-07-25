def add_asset(self, basename, file_path):
    """
    Adds an asset file to the assets dictionary using basename as key and file_path as value.
    
    Args:
        basename (str): Base filename to use as key
        file_path (str): Full file path to use as value
        
    Returns:
        None
    """
    if not hasattr(self, 'assets'):
        self.assets = {}
        
    self.assets[basename] = file_path