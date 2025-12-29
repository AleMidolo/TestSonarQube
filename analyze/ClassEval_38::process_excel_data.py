def process_excel_data(self, N, save_file_name):
    """
        Change the specified column in the Excel file to uppercase
        :param N: int, The serial number of the column that want to change
        :param save_file_name: str, source file name
        :return:(int, str), The former is the return value of write_excel, while the latter is the saved file name of the processed data
        >>> processor = ExcelProcessor()
        >>> success, output_file = processor.process_excel_data(1, 'test_data.xlsx')
        """
    try:
        data = self.read_excel(save_file_name)
        if data is None:
            return (0, '')
        col_index = N - 1
        processed_data = []
        for row in data:
            processed_row = list(row)
            if col_index < len(processed_row) and processed_row[col_index] is not None:
                if isinstance(processed_row[col_index], str):
                    processed_row[col_index] = processed_row[col_index].upper()
            processed_data.append(tuple(processed_row))
        if '.' in save_file_name:
            name_parts = save_file_name.rsplit('.', 1)
            output_file = f'{name_parts[0]}_processed.{name_parts[1]}'
        else:
            output_file = f'{save_file_name}_processed.xlsx'
        result = self.write_excel(processed_data, output_file)
        return (result, output_file)
    except Exception as e:
        return (0, '')