def process_csv_data(self, N, save_file_name):
    """
        Lee un archivo csv en las variables title y data.
        Solo se mantiene la N-ésima (desde 0) columna de datos y se capitalizan, se almacenan el título y los nuevos datos en un nuevo archivo csv.
        Se añade el sufijo '_process' después del nombre del archivo antiguo, como un nuevo nombre de archivo.
        :param N: int, la N-ésima columna (desde 0)
        :param save_file_name: el nombre del archivo que necesita ser procesado.
        :return: int, si tiene éxito devuelve 1, o 0 en caso contrario
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
        new_data = []
        for row in data:
            if N < len(row):
                new_data.append([row[N].upper()])
            else:
                new_data.append([''])
        base_name = save_file_name.rsplit('.', 1)[0]
        extension = save_file_name.rsplit('.', 1)[1] if '.' in save_file_name else 'csv'
        new_file_name = f'{base_name}_process.{extension}'
        if N < len(title):
            new_title = [title[N]]
        else:
            new_title = ['']
        return self.write_csv([new_title] + new_data, new_file_name)
    except Exception as e:
        return 0