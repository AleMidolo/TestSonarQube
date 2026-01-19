def add_table(self, data):
    """
        Agrega una tabla al documento de Word con los datos especificados.
        :param data: lista de listas, los datos para poblar la tabla.
        :return: bool, True si la tabla se agrega correctamente, False en caso contrario.
        """
    try:
        doc = Document(self.file_path)
        table = doc.add_table(rows=len(data), cols=len(data[0]) if data else 0)
        for i, row_data in enumerate(data):
            row = table.rows[i]
            for j, cell_data in enumerate(row_data):
                row.cells[j].text = str(cell_data)
        doc.save(self.file_path)
        return True
    except:
        return False