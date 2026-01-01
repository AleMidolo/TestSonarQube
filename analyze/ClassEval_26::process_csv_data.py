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
        if N < 0 or N >= len(title):
            return 0
        new_data = []
        for row in data:
            if N < len(row):
                new_data.append([row[N].upper()])
            else:
                new_data.append([''])
        base_name = save_file_name.rsplit('.', 1)[0]
        extension = save_file_name.rsplit('.', 1)[1] if '.' in save_file_name else 'csv'
        output_file_name = f'{base_name}_process.{extension}'
        new_title = [title[N]]
        output_data = [new_title] + new_data
        return self.write_csv(output_data, output_file_name)
    except Exception as e:
        return 0