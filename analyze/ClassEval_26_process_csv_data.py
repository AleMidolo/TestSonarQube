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
        # Read the CSV file
        result = self.read_csv(save_file_name)
        if result == 0:
            return 0
        
        title, data = result
        
        # Check if N is valid
        if N < 0 or N >= len(title):
            return 0
        
        # Process data: keep only N-th column and capitalize
        processed_data = []
        for row in data:
            if N < len(row):
                processed_data.append([row[N].upper()])
            else:
                return 0
        
        # Create new filename with '_process' suffix
        if '.' in save_file_name:
            name_parts = save_file_name.rsplit('.', 1)
            new_file_name = name_parts[0] + '_process.' + name_parts[1]
        else:
            new_file_name = save_file_name + '_process'
        
        # Write to new CSV file
        self.write_csv(title, processed_data, new_file_name)
        
        return 1
    except:
        return 0