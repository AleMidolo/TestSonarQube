def _get_err_indices(self, coord_name):
    """
    Get error indices corresponding to a coordinate.
    
    Args:
        coord_name (str): The name of the coordinate.
    
    Returns:
        list: A list of indices where errors are found for the given coordinate.
    """
    err_indices = []
    for i, coord in enumerate(self.coordinates):
        if coord.name == coord_name and coord.error:
            err_indices.append(i)
    return err_indices