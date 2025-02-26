def _get_err_indices(self, coord_name):
    """
    Obtener los índices de error correspondientes a una coordenada.
    """
    # Suponiendo que self.errors es un diccionario que mapea nombres de coordenadas a listas de índices de error
    if coord_name in self.errors:
        return self.errors[coord_name]
    else:
        return []