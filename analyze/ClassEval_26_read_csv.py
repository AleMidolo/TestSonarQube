def read_csv(self, file_name):
    """
        Lee el archivo csv por file_name, obtiene el título y los datos de él
        :param file_name: str, nombre del archivo csv
        :return title, data: (list, list), la primera fila es el título, el resto son datos
        >>> csvProcessor = CSVProcessor()
        >>> csvProcessor.read_csv('read_test.csv')
        (['a', 'b', 'c', 'd'], [['hElLo', 'YoU', 'ME', 'LoW']])
        """
    try:
        with open(file_name, 'r', newline='') as file:
            reader = csv.reader(file)
            title = next(reader)
            data = [row for row in reader]
        return (title, data)
    except:
        return ([], [])