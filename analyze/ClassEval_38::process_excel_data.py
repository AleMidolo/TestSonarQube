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
            new_row = list(row)
            if 0 <= N - 1 < len(new_row):
                cell_value = new_row[N - 1]
                if isinstance(cell_value, str):
                    new_row[N - 1] = cell_value.upper()
            processed_data.append(tuple(new_row))
        output_file = f'processed_{save_file_name}'
        result = self.write_excel(processed_data, output_file)
        return (result, output_file)
    except:
        return (0, '')