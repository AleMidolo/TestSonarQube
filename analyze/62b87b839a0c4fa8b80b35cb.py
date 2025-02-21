def _get_err_indices(self, coord_name):
    """
    Ottieni gli indici di errore corrispondenti a una coordinata.
    """
    err_indices = []
    for index, coord in enumerate(self.coordinates):
        if coord.name == coord_name and coord.has_error:
            err_indices.append(index)
    return err_indices