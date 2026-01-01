def read_csv(self, file_name):
    """
        Leggi il file csv tramite file_name, ottieni il titolo e i dati da esso
        :param file_name: str, nome del file csv
        :return title, data: (list, list), la prima riga è il titolo, il resto sono i dati
        >>> csvProcessor = CSVProcessor()
        >>> csvProcessor.read_csv('read_test.csv')
        (['a', 'b', 'c', 'd'], [['hElLo', 'YoU', 'ME', 'LoW']])
        """
    try:
        with open(file_name, 'r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)
            if not rows:
                return ([], [])
            title = rows[0]
            data = rows[1:]
            return (title, data)
    except:
        return ([], [])