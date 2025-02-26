def add_asset(self, basename, file_path):
    """
    Adds an asset to the internal storage with the given basename and file path.
    
    The function will create entries for different file formats based on the basename.
    
    Example:
    {
        "artigo02-gf03.tiff": "/path/artigo02-gf03.tiff",
        "artigo02-gf03.jpg": "/path/artigo02-gf03.jpg",
        "artigo02-gf03.png": "/path/artigo02-gf03.png"
    }
    """
    formats = ['tiff', 'jpg', 'png']
    assets = {}
    
    for fmt in formats:
        asset_name = f"{basename}.{fmt}"
        assets[asset_name] = file_path
    
    # Assuming there's a dictionary or similar structure to store the assets
    self.assets.update(assets)