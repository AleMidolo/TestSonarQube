def add_asset(self, basename, file_path):
    """
    {
        "artigo02-gf03.tiff": "/path/artigo02-gf03.tiff",
        "artigo02-gf03.jpg": "/path/artigo02-gf03.jpg",
        "artigo02-gf03.png": "/path/artigo02-gf03.png"
    }
    """
    if not hasattr(self, 'assets'):
        self.assets = {}
    
    file_extension = file_path.split('.')[-1]
    asset_key = f"{basename}.{file_extension}"
    self.assets[asset_key] = file_path