def process_excel_data(self, N, save_file_name):
    """
        Cambia la colonna specificata nel file Excel in maiuscolo
        :param N: int, Il numero seriale della colonna che si desidera cambiare
        :param save_file_name: str, nome del file sorgente
        :return:(int, str), Il primo è il valore di ritorno di write_excel, mentre il secondo è il nome del file salvato dei dati elaborati
        >>> processor = ExcelProcessor()
        >>> success, output_file = processor.process_excel_data(1, 'test_data.xlsx')
        """
    try:
        data = self.read_excel(save_file_name)
        if data is None:
            return (0, '')
        processed_data = []
        for row in data:
            processed_row = list(row)
            if N >= 1 and N <= len(processed_row):
                cell_value = processed_row[N - 1]
                if isinstance(cell_value, str):
                    processed_row[N - 1] = cell_value.upper()
            processed_data.append(tuple(processed_row))
        output_file = f'processed_{save_file_name}'
        result = self.write_excel(processed_data, output_file)
        return (result, output_file)
    except:
        return (0, '')