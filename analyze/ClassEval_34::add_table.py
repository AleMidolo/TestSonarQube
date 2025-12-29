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
        rows = len(data)
        cols = len(data[0]) if rows > 0 else 0
        table = doc.add_table(rows=rows, cols=cols)
        for i, row_data in enumerate(data):
            row_cells = table.rows[i].cells
            for j, cell_data in enumerate(row_data):
                if j < len(row_cells):
                    row_cells[j].text = str(cell_data)
        doc.save(self.file_path)
        return True
    except:
        return False