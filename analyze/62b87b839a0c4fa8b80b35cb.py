def _get_err_indices(self, coord_name):
    """
    Get error indices corresponding to a coordinate.
    """
    if coord_name == 'x':
        return [0, 3, 4]
    elif coord_name == 'y': 
        return [1, 3, 5]
    elif coord_name == 'z':
        return [2, 4, 5]
    else:
        raise ValueError(f"Invalid coordinate name: {coord_name}")