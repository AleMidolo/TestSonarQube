def add_asset(self, basename, file_path):
    """
    {
        "artigo02-gf03.tiff": "/path/artigo02-gf03.tiff",
        "artigo02-gf03.jpg": "/path/artigo02-gf03.jpg",
        "artigo02-gf03.png": "/path/artigo02-gf03.png"
    }
    """
    # Assuming self.assets is a dictionary to store the assets
    if not hasattr(self, 'assets'):
        self.assets = {}
    
    # Extracting the file extension
    file_extension = file_path.split('.')[-1]
    
    # Creating the asset key
    asset_key = f"{basename}.{file_extension}"
    
    # Adding the asset to the dictionary
    self.assets[asset_key] = file_path