def _get_err_indices(self, coord_name):
    """
    Get error indices corresponding to a coordinate.
    """
    # Assuming self.errors is a dictionary where keys are coordinate names
    # and values are lists of indices where errors occurred.
    if coord_name in self.errors:
        return self.errors[coord_name]
    else:
        return []