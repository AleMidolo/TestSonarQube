def add_asset(self, basename, file_path):
    """
    Adds an asset to the object's asset dictionary. The basename is used as the key,
    and the file_path is the value. This allows for easy lookup of file paths based on
    the basename.

    Args:
        basename (str): The base name of the asset (e.g., "artigo02-gf03").
        file_path (str): The full path to the asset file.

    Returns:
        None
    """
    if not hasattr(self, 'assets'):
        self.assets = {}
    
    self.assets[basename] = file_path