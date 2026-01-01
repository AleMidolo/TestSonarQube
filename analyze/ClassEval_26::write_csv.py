def write_csv(self, data, file_name):
    """
        Escribir datos en un archivo csv.
        :param file_name: str, nombre del archivo csv
        :return:int, si tiene éxito devuelve 1, o 0 en caso contrario
        >>> csvProcessor = CSVProcessor()
        >>> csvProcessor.write_csv([['a', 'b', 'c', 'd'], ['1', '2', '3', '4']], 'write_test.csv')
        1
        """
    try:
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        return 1
    except Exception as e:
        return 0