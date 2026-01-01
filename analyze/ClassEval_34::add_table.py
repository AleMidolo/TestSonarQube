def add_table(self, data):
    """
    Agrega una tabla al documento de Word con los datos especificados.
    :param data: lista de listas, los datos para poblar la tabla.
    :return: bool, True si la tabla se agrega correctamente, False en caso contrario.
    """
    try:
        doc = Document(self.file_path)
        table = doc.add_table(rows=len(data), cols=len(data[0]))
        for i, row in enumerate(data):
            for j, cell in enumerate(row):
                table.cell(i, j).text = str(cell)
        doc.save(self.file_path)
        return True
    except:
        return False