def add_table(self, data):
    """
    Agrega una tabla al documento de Word con los datos especificados.
    :param data: lista de listas, los datos para poblar la tabla.
    :return: bool, True si la tabla se agrega correctamente, False en caso contrario.
    """
    try:
        if not data or len(data) == 0:
            return False
        
        # Determinar el número de filas y columnas
        rows = len(data)
        cols = len(data[0]) if data[0] else 0
        
        if cols == 0:
            return False
        
        # Crear la tabla en el documento
        table = self.document.add_table(rows=rows, cols=cols)
        table.style = 'Table Grid'
        
        # Poblar la tabla con los datos
        for i, row_data in enumerate(data):
            row_cells = table.rows[i].cells
            for j, cell_data in enumerate(row_data):
                if j < cols:
                    row_cells[j].text = str(cell_data)
        
        return True
    except Exception as e:
        return False