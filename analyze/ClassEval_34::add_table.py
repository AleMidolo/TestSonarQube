def add_table(self, data):
    """
        Aggiunge una tabella al documento Word con i dati specificati.
        :param data: lista di liste, i dati per popolare la tabella.
        :return: bool, True se la tabella è stata aggiunta con successo, False altrimenti.
        """
    try:
        doc = Document(self.file_path)
        if not data or not isinstance(data, list):
            return False
        num_rows = len(data)
        if num_rows == 0:
            return False
        num_cols = len(data[0]) if isinstance(data[0], list) else 1
        table = doc.add_table(rows=num_rows, cols=num_cols)
        for i, row_data in enumerate(data):
            if i >= num_rows:
                break
            if isinstance(row_data, list):
                for j, cell_data in enumerate(row_data):
                    if j < num_cols:
                        table.cell(i, j).text = str(cell_data)
            else:
                table.cell(i, 0).text = str(row_data)
        doc.save(self.file_path)
        return True
    except:
        return False