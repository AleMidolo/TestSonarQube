def _get_err_indices(self, coord_name):
    """
    Ottieni gli indici di errore corrispondenti a una coordinata.
    """
    # Assuming we have a dictionary of coordinates with their corresponding error indices
    error_indices = {
        'x': [0, 1, 2],
        'y': [3, 4, 5],
        'z': [6, 7, 8]
    }
    
    return error_indices.get(coord_name, [])