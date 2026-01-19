def read_csv(self, file_name):
    """
    Lee el archivo csv por file_name, obtiene el título y los datos de él
    :param file_name: str, nombre del archivo csv
    :return title, data: (list, list), la primera fila es el título, el resto son datos
    >>> csvProcessor = CSVProcessor()
    >>> csvProcessor.read_csv('read_test.csv')
    (['a', 'b', 'c', 'd'], [['hElLo', 'YoU', 'ME', 'LoW']])
    """
    import csv
    
    with open(file_name, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        rows = list(csv_reader)
        
        if len(rows) == 0:
            return [], []
        
        title = rows[0]
        data = rows[1:]
        
        return title, data