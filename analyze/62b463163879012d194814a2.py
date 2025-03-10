def add_asset(self, basename, file_path):
    """
    Adds an asset to the object's asset dictionary using the provided basename and file path.
    
    Args:
        basename (str): The base name of the asset (e.g., "artigo02-gf03").
        file_path (str): The full path to the asset file.
    
    Returns:
        None
    """
    if not hasattr(self, 'assets'):
        self.assets = {}
    
    # Generate the asset keys based on the basename and supported extensions
    extensions = ['.tiff', '.jpg', '.png']
    for ext in extensions:
        key = f"{basename}{ext}"
        self.assets[key] = file_path