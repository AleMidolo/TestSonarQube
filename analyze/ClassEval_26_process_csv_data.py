def process_csv_data(self, N, save_file_name):
    """
   Legge un file CSV e ne carica titolo e dati.
Mantiene solo la colonna N (a partire da 0), ne converte i valori in maiuscolo
e salva titolo e nuovi dati in un nuovo file CSV.
Al nome del file originale viene aggiunto il suffisso '_process'.
    :param N: int, la N-esima colonna (da 0)
    :param save_file_name, il nome del file che deve essere elaborato.
    :return:int, se ha successo restituisce 1, altrimenti 0
    >>> csvProcessor = CSVProcessor()
    >>> csvProcessor.read_csv('read_test.csv')
    (['a', 'b', 'c', 'd'], [['hElLo', 'YoU', 'ME', 'LoW']])
    >>> csvProcessor.process_csv_data(0, 'read_test.csv')
    1
    >>> csvProcessor.read_csv('read_test_process.csv')
    (['a', 'b', 'c', 'd'], [['HELLO']])
    """
    try:
        # Legge il file CSV
        result = self.read_csv(save_file_name)
        if result is None:
            return 0
        
        title, data = result
        
        # Verifica che N sia un indice valido
        if N < 0 or N >= len(title):
            return 0
        
        # Processa i dati: mantiene solo la colonna N e converte in maiuscolo
        processed_data = []
        for row in data:
            if N < len(row):
                processed_data.append([row[N].upper()])
        
        # Crea il nome del nuovo file aggiungendo '_process' prima dell'estensione
        if '.' in save_file_name:
            name_parts = save_file_name.rsplit('.', 1)
            new_file_name = name_parts[0] + '_process.' + name_parts[1]
        else:
            new_file_name = save_file_name + '_process'
        
        # Salva i dati processati nel nuovo file
        self.write_csv(new_file_name, title, processed_data)
        
        return 1
    except:
        return 0