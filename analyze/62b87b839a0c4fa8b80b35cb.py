def _get_err_indices(self, coord_name):
    """
    Ottieni gli indici di errore corrispondenti a una coordinata.
    """
    # Supponiamo che self.errors sia un dizionario che mappa i nomi delle coordinate agli indici di errore
    if coord_name in self.errors:
        return self.errors[coord_name]
    else:
        return []