def add_asset(self, basename, file_path):
    """Adds an asset file path mapping to the assets dictionary.
    
    Args:
        basename (str): Base filename without extension
        file_path (str): Full file path to the asset
        
    Returns:
        dict: Updated assets dictionary with new mapping
    """
    # Get file extension
    extension = file_path.split('.')[-1].lower()
    
    # Create key with basename and extension
    key = f"{basename}.{extension}"
    
    # Add to assets dictionary
    if not hasattr(self, 'assets'):
        self.assets = {}
    self.assets[key] = file_path
    
    return self.assets