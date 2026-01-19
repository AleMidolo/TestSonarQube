def write_csv(self, data, file_name):
    """
        Scrivi i dati in un file csv.
        :param file_name: str, nome del file csv
        :return:int, se ha successo restituisce 1, altrimenti 0
        >>> csvProcessor = CSVProcessor()
        >>> csvProcessor.write_csv([['a', 'b', 'c', 'd'], ['1', '2', '3', '4']], 'write_test.csv')
        1
        """
    try:
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        return 1
    except Exception:
        return 0