def add_asset(self, basename, file_path):
    """
    Adds an asset to the object with the given basename and file path.
    
    Args:
        basename (str): The base name of the asset.
        file_path (str): The file path of the asset.
    
    Returns:
        dict: A dictionary containing the asset mappings.
    """
    asset_dict = {
        f"{basename}.tiff": f"{file_path}/{basename}.tiff",
        f"{basename}.jpg": f"{file_path}/{basename}.jpg",
        f"{basename}.png": f"{file_path}/{basename}.png"
    }
    return asset_dict