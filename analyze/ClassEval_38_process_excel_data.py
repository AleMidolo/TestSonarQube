def process_excel_data(self, N, save_file_name):
    """
    Change the specified column in the Excel file to uppercase
    :param N: int, The serial number of the column that want to change
    :param save_file_name: str, source file name
    :return:(int, str), The former is the return value of write_excel, while the latter is the saved file name of the processed data
    >>> processor = ExcelProcessor()
    >>> success, output_file = processor.process_excel_data(1, 'test_data.xlsx')
    """
    import openpyxl
    
    # Read the Excel file
    try:
        workbook = openpyxl.load_workbook(save_file_name)
        sheet = workbook.active
        
        # Process the specified column (N is 1-indexed)
        for row in sheet.iter_rows(min_row=1, min_col=N, max_col=N):
            for cell in row:
                if cell.value is not None and isinstance(cell.value, str):
                    cell.value = cell.value.upper()
        
        # Save the modified workbook
        output_file_name = f"processed_{save_file_name}"
        workbook.save(output_file_name)
        workbook.close()
        
        # Assuming write_excel returns 1 for success
        return (1, output_file_name)
    except Exception as e:
        # Return 0 for failure
        return (0, save_file_name)