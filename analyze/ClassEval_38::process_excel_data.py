def process_excel_data(self, N, save_file_name):
    """
        Cambia la columna especificada en el archivo de Excel a mayúsculas
        :param N: int, El número de serie de la columna que se desea cambiar
        :param save_file_name: str, nombre del archivo fuente
        :return:(int, str), El primero es el valor de retorno de write_excel, mientras que el segundo es el nombre del archivo guardado de los datos procesados
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
            output_file = f'{name_parts[0]}_processed.{name_parts[1]}'
        else:
            output_file = f'{save_file_name}_processed.xlsx'
        result = self.write_excel(processed_data, output_file)
        return (result, output_file)
    except Exception:
        return (0, '')