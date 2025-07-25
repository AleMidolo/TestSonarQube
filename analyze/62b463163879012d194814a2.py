def add_asset(self, basename, file_path):
    """
    Adds an asset to the internal storage with the given basename and file path.
    
    The function expects a dictionary format where the key is the asset name 
    and the value is the corresponding file path.
    
    Example:
    {
        "artigo02-gf03.tiff": "/path/artigo02-gf03.tiff",
        "artigo02-gf03.jpg": "/path/artigo02-gf03.jpg",
        "artigo02-gf03.png": "/path/artigo02-gf03.png"
    }
    """
    if not hasattr(self, 'assets'):
        self.assets = {}
    
    self.assets[basename] = file_path