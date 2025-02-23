def add_asset(self, basename, file_path):
    """
    Adds an asset to the internal storage with the given basename and file path.
    
    The function expects a basename and a file path, and it will store the asset
    in a dictionary format where the key is the basename and the value is the file path.
    
    Example:
    {
        "artigo02-gf03.tiff": "/path/artigo02-gf03.tiff",
        "artigo02-gf03.jpg": "/path/artigo02-gf03.jpg",
        "artigo02-gf03.png": "/path/artigo02-gf03.png"
    }
    """
    if not hasattr(self, 'assets'):
        self.assets = {}
    
    # Extract the file extension
    file_extension = file_path.split('.')[-1]
    
    # Create the full asset name
    asset_name = f"{basename}.{file_extension}"
    
    # Add the asset to the dictionary
    self.assets[asset_name] = file_path