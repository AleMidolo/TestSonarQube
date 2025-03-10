def _get_err_indices(self, coord_name):
    """
    Get error indices corresponding to a coordinate.
    
    Args:
        coord_name (str): The name of the coordinate for which to retrieve error indices.
    
    Returns:
        list: A list of indices where errors are detected for the specified coordinate.
    """
    # Assuming self.errors is a dictionary where keys are coordinate names and values are lists of error indices
    if coord_name in self.errors:
        return self.errors[coord_name]
    else:
        return []