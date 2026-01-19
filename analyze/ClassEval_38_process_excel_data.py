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
    
    # Process the specified column (N is 1-indexed)
    # Convert column N to uppercase
    for row in data:
        if len(row) >= N and row[N-1] is not None:
            if isinstance(row[N-1], str):
                row[N-1] = row[N-1].upper()
    
    # Write the processed data to the save file
    result = self.write_excel(data, save_file_name)
    
    return (result, save_file_name)