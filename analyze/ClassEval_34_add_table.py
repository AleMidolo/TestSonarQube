def add_table(self, data):
    """
    Aggiunge una tabella al documento Word con i dati specificati.
    :param data: lista di liste, i dati per popolare la tabella.
    :return: bool, True se la tabella è stata aggiunta con successo, False altrimenti.
    """
    try:
        if not data or not isinstance(data, list):
            return False
        
        # Verifica che tutti gli elementi siano liste
        if not all(isinstance(row, list) for row in data):
            return False
        
        # Verifica che ci siano righe e colonne
        if len(data) == 0:
            return False
        
        num_rows = len(data)
        num_cols = len(data[0]) if data else 0
        
        if num_cols == 0:
            return False
        
        # Crea la tabella nel documento (assumendo che self.document sia un oggetto python-docx)
        table = self.document.add_table(rows=num_rows, cols=num_cols)
        
        # Popola la tabella con i dati
        for i, row_data in enumerate(data):
            row_cells = table.rows[i].cells
            for j, cell_value in enumerate(row_data):
                if j < num_cols:
                    row_cells[j].text = str(cell_value)
        
        return True
        
    except Exception as e:
        return False