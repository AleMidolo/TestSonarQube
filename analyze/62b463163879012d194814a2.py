def add_asset(self, basename, file_path):
    """
    Adds an asset file to the assets dictionary.
    
    Args:
        basename (str): Base filename without extension
        file_path (str): Full path to the asset file
        
    Returns:
        dict: Updated assets dictionary mapping filenames to paths
    """
    # Get file extension from path
    extension = file_path.split('.')[-1].lower()
    
    # Create filename with extension
    filename = f"{basename}.{extension}"
    
    # Add to assets dict
    if not hasattr(self, 'assets'):
        self.assets = {}
    self.assets[filename] = file_path
    
    return self.assets