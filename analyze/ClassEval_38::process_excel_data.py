def process_excel_data(self, N, save_file_name):
    """
        Change the specified column in the Excel file to uppercase
        :param N: int, The serial number of the column that want to change
        :param save_file_name: str, source file name
        :return:(int, str), The former is the return value of write_excel, while the latter is the saved file name of the processed data
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
            processed_row[N - 1] = str(processed_row[N - 1]).upper()
        processed_data.append(tuple(processed_row))
    output_file = save_file_name.replace('.xlsx', '_processed.xlsx')
    if output_file == save_file_name:
        output_file = save_file_name.replace('.xls', '_processed.xlsx')
    success = self.write_excel(processed_data, output_file)
    return (success, output_file)