def _get_err_indices(self, coord_name):
    """
    Ottieni gli indici di errore corrispondenti a una coordinata.
    """
    # Dizionario che mappa le coordinate agli indici di errore
    err_index_map = {
        'x': [0, 3, 4],  # errori relativi a x: ex, exy, exz
        'y': [1, 3, 5],  # errori relativi a y: ey, exy, eyz  
        'z': [2, 4, 5]   # errori relativi a z: ez, exz, eyz
    }
    
    # Restituisce gli indici di errore per la coordinata specificata
    if coord_name in err_index_map:
        return err_index_map[coord_name]
    else:
        raise ValueError(f"Coordinata non valida: {coord_name}")