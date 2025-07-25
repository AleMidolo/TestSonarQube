def add_asset(self, basename, file_path):
    """
    Adds an asset to the instance's asset dictionary with the given basename and file path.
    
    Args:
        basename (str): The base name of the asset (e.g., "artigo02-gf03").
        file_path (str): The full path to the asset file.
    
    Returns:
        None
    """
    if not hasattr(self, 'assets'):
        self.assets = {}
    
    # Generate keys for different file formats
    self.assets[f"{basename}.tiff"] = file_path
    self.assets[f"{basename}.jpg"] = file_path
    self.assets[f"{basename}.png"] = file_path