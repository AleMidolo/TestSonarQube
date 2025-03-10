def _get_err_indices(self, coord_name):
    """
    Get error indices corresponding to a coordinate.
    
    Args:
        coord_name (str): The name of the coordinate for which to retrieve error indices.
    
    Returns:
        list: A list of indices where errors are present for the specified coordinate.
    """
    if not hasattr(self, 'errors'):
        return []
    
    if coord_name not in self.errors:
        return []
    
    return [i for i, val in enumerate(self.errors[coord_name]) if val is not None]