def add_asset(self, basename, file_path):
    """Adds an asset file path to the assets dictionary using the basename as key.
    
    Args:
        basename (str): Base filename to use as key
        file_path (str): Full file path to the asset
        
    Returns:
        None
        
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