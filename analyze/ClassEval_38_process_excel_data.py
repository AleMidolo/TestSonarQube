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
            if 0 <= N - 1 < len(processed_row):
                cell_value = processed_row[N - 1]
                if isinstance(cell_value, str):
                    processed_row[N - 1] = cell_value.upper()
            processed_data.append(tuple(processed_row))
        if '.' in save_file_name:
            name_parts = save_file_name.rsplit('.', 1)
            output_file_name = f'{name_parts[0]}_processed.{name_parts[1]}'
        else:
            output_file_name = f'{save_file_name}_processed.xlsx'
        result = self.write_excel(processed_data, output_file_name)
        return (result, output_file_name)
    except Exception as e:
        return (0, '')