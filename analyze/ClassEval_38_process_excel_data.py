def process_excel_data(self, N, save_file_name):
    """
        Cambia la columna especificada en el archivo de Excel a mayúsculas
        :param N: int, El número de serie de la columna que se desea cambiar
        :param save_file_name: str, nombre del archivo fuente
        :return:(int, str), El primero es el valor de retorno de write_excel, mientras que el segundo es el nombre del archivo guardado de los datos procesados
        >>> processor = ExcelProcessor()
        >>> success, output_file = processor.process_excel_data(1, 'test_data.xlsx')
        """
    data = self.read_excel(save_file_name)
    if data is None:
        return (0, '')
    processed_data = []
    for row in data:
        processed_row = list(row)
        if N - 1 < len(processed_row) and processed_row[N - 1] is not None:
            if isinstance(processed_row[N - 1], str):
                processed_row[N - 1] = processed_row[N - 1].upper()
        processed_data.append(tuple(processed_row))
    output_file_name = f'processed_{save_file_name}'
    result = self.write_excel(processed_data, output_file_name)
    return (result, output_file_name)