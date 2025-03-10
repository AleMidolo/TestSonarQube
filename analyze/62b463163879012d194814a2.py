def add_asset(self, basename, file_path):
    """
    Adds an asset to the instance's asset dictionary.

    Args:
        basename (str): The base name of the asset.
        file_path (str): The file path of the asset.

    Returns:
        None
    """
    if not hasattr(self, 'assets'):
        self.assets = {}
    
    self.assets[basename] = file_path