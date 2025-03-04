def _get_err_indices(self, coord_name):
    """
    Ottieni gli indici di errore corrispondenti a una coordinata.
    """
    # Dictionary mapping coordinate names to their error indices
    err_index_map = {
        'x': 0,
        'y': 1,
        'z': 2,
        'roll': 3,
        'pitch': 4,
        'yaw': 5
    }
    
    # Return the error index for the given coordinate name
    # If coordinate name not found, raise ValueError
    if coord_name in err_index_map:
        return err_index_map[coord_name]
    else:
        raise ValueError(f"Invalid coordinate name: {coord_name}")