def process_excel_data(self, N, save_file_name):
    """
    Cambia la colonna specificata nel file Excel in maiuscolo
    :param N: int, Il numero seriale della colonna che si desidera cambiare
    :param save_file_name: str, nome del file sorgente
    :return:(int, str), Il primo è il valore di ritorno di write_excel, mentre il secondo è il nome del file salvato dei dati elaborati
    >>> processor = ExcelProcessor()
    >>> success, output_file = processor.process_excel_data(1, 'test_data.xlsx')
    """
    import openpyxl
    import os
    
    # Read the Excel file
    try:
        workbook = openpyxl.load_workbook(save_file_name)
        sheet = workbook.active
        
        # Convert the specified column (N) to uppercase
        # N is 1-indexed (1 = column A, 2 = column B, etc.)
        for row in sheet.iter_rows(min_row=1, min_col=N, max_col=N):
            for cell in row:
                if cell.value is not None and isinstance(cell.value, str):
                    cell.value = cell.value.upper()
        
        # Generate output file name
        base_name = os.path.splitext(save_file_name)[0]
        extension = os.path.splitext(save_file_name)[1]
        output_file_name = f"{base_name}_processed{extension}"
        
        # Save the workbook
        workbook.save(output_file_name)
        workbook.close()
        
        # Assuming write_excel returns 1 for success
        return (1, output_file_name)
        
    except Exception as e:
        # Return 0 for failure
        return (0, "")