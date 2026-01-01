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
        title, data = self.read_csv(save_file_name)
        new_data = [[row[N].upper()] for row in data]
        new_file_name = save_file_name.replace('.csv', '_process.csv')
        self.write_csv([title] + new_data, new_file_name)
        return 1
    except Exception as e:
        return 0