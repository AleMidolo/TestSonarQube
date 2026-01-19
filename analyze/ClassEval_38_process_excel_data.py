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
    self.read_excel(save_file_name)
    
    # Convert the specified column (N) to uppercase
    # N is 1-indexed, so we need to adjust for 0-indexed list
    if self.data and len(self.data) > 0:
        for row in self.data:
            if len(row) >= N and N > 0:
                # Convert the value at column N to uppercase if it's a string
                if isinstance(row[N - 1], str):
                    row[N - 1] = row[N - 1].upper()
    
    # Generate output filename
    output_file_name = save_file_name.replace('.xlsx', '_processed.xlsx')
    
    # Write the processed data back to Excel
    result = self.write_excel(output_file_name)
    
    return (result, output_file_name)