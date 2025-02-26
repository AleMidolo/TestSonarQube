def add_asset(self, basename, file_path):
    """
    Adds an asset to the internal storage with the given basename and file path.
    
    The function will create a mapping of the basename with different file extensions
    to their respective file paths. The supported extensions are .tiff, .jpg, and .png.
    
    Example:
    {
        "artigo02-gf03.tiff": "/path/artigo02-gf03.tiff",
        "artigo02-gf03.jpg": "/path/artigo02-gf03.jpg",
        "artigo02-gf03.png": "/path/artigo02-gf03.png"
    }
    """
    extensions = ['.tiff', '.jpg', '.png']
    asset_map = {}
    
    for ext in extensions:
        asset_map[f"{basename}{ext}"] = file_path
    
    # Assuming there's a dictionary attribute to store assets
    if not hasattr(self, 'assets'):
        self.assets = {}
    
    self.assets.update(asset_map)