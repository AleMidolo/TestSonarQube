def add_asset(self, basename, file_path):
    """
    Adds an asset to the object's asset dictionary. The asset is stored with the basename as the key and the file path as the value.

    Args:
        basename (str): The base name of the asset (e.g., "artigo02-gf03").
        file_path (str): The full path to the asset file.

    Returns:
        None
    """
    if not hasattr(self, 'assets'):
        self.assets = {}
    
    self.assets[f"{basename}.tiff"] = f"{file_path}/{basename}.tiff"
    self.assets[f"{basename}.jpg"] = f"{file_path}/{basename}.jpg"
    self.assets[f"{basename}.png"] = f"{file_path}/{basename}.png"