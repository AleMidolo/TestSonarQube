def _get_err_indices(self, coord_name):
    """
    Obtener los índices de error correspondientes a una coordenada.
    """
    # Assuming self.errors is a dictionary where keys are coordinate names
    # and values are lists of error indices.
    if coord_name in self.errors:
        return self.errors[coord_name]
    else:
        return []