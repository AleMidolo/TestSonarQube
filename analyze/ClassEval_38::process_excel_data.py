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
            if row is None:
                processed_data.append(row)
                continue
            row_list = list(row)
            if col_index < len(row_list):
                if isinstance(row_list[col_index], str):
                    row_list[col_index] = row_list[col_index].upper()
            processed_data.append(tuple(row_list))
        if '.' in save_file_name:
            name_parts = save_file_name.rsplit('.', 1)
            output_file = f'{name_parts[0]}_processed.{name_parts[1]}'
        else:
            output_file = f'{save_file_name}_processed.xlsx'
        result = self.write_excel(processed_data, output_file)
        return (result, output_file)
    except Exception as e:
        return (0, '')