def add_table(self, data):
    """
    Aggiunge una tabella al documento Word con i dati specificati.
    :param data: lista di liste, i dati per popolare la tabella.
    :return: bool, True se la tabella è stata aggiunta con successo, False altrimenti.
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