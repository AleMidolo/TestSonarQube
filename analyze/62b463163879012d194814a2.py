def add_asset(self, basename, file_path):
    """
    Adds an asset to the object's asset dictionary. The asset is identified by its basename and file path.

    Args:
        basename (str): The base name of the asset (e.g., "artigo02-gf03").
        file_path (str): The full path to the asset file.

    Returns:
        None
    """
    if not hasattr(self, 'assets'):
        self.assets = {}
    
    # Assuming the basename is used as a key and the file_path as the value
    self.assets[basename] = file_path