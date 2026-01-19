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
    import csv
    import os
    
    try:
        # Read the CSV file
        result = self.read_csv(save_file_name)
        if result is None:
            return 0
        
        title, data = result
        
        # Check if N is valid
        if N < 0 or N >= len(title):
            return 0
        
        # Process data: keep only Nth column and capitalize
        processed_data = []
        for row in data:
            if N < len(row):
                processed_data.append([row[N].upper()])
        
        # Generate new file name with '_process' suffix
        base_name, ext = os.path.splitext(save_file_name)
        new_file_name = base_name + '_process' + ext
        
        # Write to new CSV file
        with open(new_file_name, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(title)
            writer.writerows(processed_data)
        
        return 1
    except Exception as e:
        return 0