def process_excel_data(self, N, save_file_name):
    """
    Change the specified column in the Excel file to uppercase
    :param N: int, The serial number of the column that want to change
    :param save_file_name: str, source file name
    :return:(int, str), The former is the return value of write_excel, while the latter is the saved file name of the processed data
    >>> processor = ExcelProcessor()
    >>> success, output_file = processor.process_excel_data(1, 'test_data.xlsx')
    """
    # Read the Excel file
    data = self.read_excel()
    
    if data is None or len(data) == 0:
        return (0, save_file_name)
    
    # Convert the specified column (N) to uppercase
    # N is 1-indexed, so we need to use N-1 for 0-indexed list
    for row in data:
        if len(row) >= N and row[N-1] is not None:
            # Convert to string and then to uppercase
            row[N-1] = str(row[N-1]).upper()
    
    # Write the modified data to the Excel file
    result = self.write_excel(data, save_file_name)
    
    return (result, save_file_name)