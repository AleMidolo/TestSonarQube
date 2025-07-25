def add_asset(self, basename, file_path):
    """
    Adds an asset to the internal storage with the given basename and file path.
    
    The function will create entries for different file formats based on the basename.
    
    Args:
        basename (str): The base name of the asset without the extension.
        file_path (str): The path to the asset file.
    
    Returns:
        dict: A dictionary mapping file names to their respective paths.
    """
    extensions = ['tiff', 'jpg', 'png']
    asset_dict = {}
    
    for ext in extensions:
        asset_name = f"{basename}.{ext}"
        asset_dict[asset_name] = file_path
    
    return asset_dict