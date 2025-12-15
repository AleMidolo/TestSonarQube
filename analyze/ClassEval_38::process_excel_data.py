def process_excel_data(self, N, save_file_name):
    """
    Cambia la colonna specificata nel file Excel in maiuscolo
    :param N: int, Il numero seriale della colonna che si desidera cambiare
    :param save_file_name: str, nome del file sorgente
    :return:(int, str), Il primo è il valore di ritorno di write_excel, mentre il secondo è il nome del file salvato dei dati elaborati
    >>> processor = ExcelProcessor()
    >>> success, output_file = processor.process_excel_data(1, 'test_data.xlsx')
    """
    
    data = self.read_excel(save_file_name)
    if data is None or N < 1 or N > len(data[0]):
        return 0, save_file_name
    
    # Convert the specified column to uppercase
    column_index = N - 1
    for i in range(len(data)):
        row = list(data[i])
        row[column_index] = str(row[column_index]).upper()
        data[i] = tuple(row)
    
    output_file_name = f"processed_{save_file_name}"
    success = self.write_excel(data, output_file_name)
    
    return success, output_file_name