def read_csv(self, file_name):
    """
    Leggi il file csv tramite file_name, ottieni il titolo e i dati da esso
    :param file_name: str, nome del file csv
    :return title, data: (list, list), la prima riga è il titolo, il resto sono i dati
    >>> csvProcessor = CSVProcessor()
    >>> csvProcessor.read_csv('read_test.csv')
    (['a', 'b', 'c', 'd'], [['hElLo', 'YoU', 'ME', 'LoW']])
    """
    import csv
    
    title = []
    data = []
    
    with open(file_name, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        title = next(csv_reader)
        data = [row for row in csv_reader]
    
    return title, data