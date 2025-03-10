def add_asset(self, basename, file_path):
    """
    Adds an asset to the internal dictionary with the given basename and file path.
    
    Args:
        basename (str): The base name of the asset (e.g., "artigo02-gf03").
        file_path (str): The full path to the asset file.
    
    Returns:
        None
    """
    if not hasattr(self, 'assets'):
        self.assets = {}
    
    # Generate the full asset name by combining basename and file extension
    import os
    file_extension = os.path.splitext(file_path)[1]
    asset_name = f"{basename}{file_extension}"
    
    # Add the asset to the dictionary
    self.assets[asset_name] = file_path