def add_table(self, data):
    """
        Aggiunge una tabella al documento Word con i dati specificati.
        :param data: lista di liste, i dati per popolare la tabella.
        :return: bool, True se la tabella è stata aggiunta con successo, False altrimenti.
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