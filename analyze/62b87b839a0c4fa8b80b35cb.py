def _get_err_indices(self, coord_name):
    """
    Ottieni gli indici di errore corrispondenti a una coordinata.
    """
    # Assuming self.errors is a dictionary where keys are coordinate names
    # and values are lists of error indices
    if coord_name in self.errors:
        return self.errors[coord_name]
    else:
        return []