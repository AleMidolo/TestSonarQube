def add_asset(self, basename, file_path):
    """
    Adds an asset to the internal storage with the given basename and file path.
    
    The asset is stored in a dictionary format where the key is the basename
    with its respective file extension and the value is the file path.
    
    Example:
    {
        "artigo02-gf03.tiff": "/path/artigo02-gf03.tiff",
        "artigo02-gf03.jpg": "/path/artigo02-gf03.jpg",
        "artigo02-gf03.png": "/path/artigo02-gf03.png",
    }
    """
    extensions = ['.tiff', '.jpg', '.png']
    asset_dict = {}
    
    for ext in extensions:
        asset_key = f"{basename}{ext}"
        asset_dict[asset_key] = file_path
    
    # Assuming there's an internal storage dictionary to hold the assets
    if not hasattr(self, 'assets'):
        self.assets = {}
    
    self.assets.update(asset_dict)