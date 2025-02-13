def _get_err_indices(self, coord_name):
    error_indices = []
    for index, coord in enumerate(self.coordinates):
        if coord.name == coord_name and coord.has_error:
            error_indices.append(index)
    return error_indices