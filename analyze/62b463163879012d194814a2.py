def add_asset(self, basename, file_path):
    """
    Adds an asset to the object's asset dictionary.

    Args:
        basename (str): The base name of the asset (e.g., "artigo02-gf03").
        file_path (str): The full path to the asset file.

    Returns:
        None
    """
    if not hasattr(self, 'assets'):
        self.assets = {}
    
    # Add the asset with its full path to the dictionary
    self.assets[f"{basename}.tiff"] = f"{file_path}.tiff"
    self.assets[f"{basename}.jpg"] = f"{file_path}.jpg"
    self.assets[f"{basename}.png"] = f"{file_path}.png"