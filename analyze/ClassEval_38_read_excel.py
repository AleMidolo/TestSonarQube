def read_excel(self, file_name):
    """
    Reading data from Excel files
    :param file_name:str, Excel file name to read
    :return:list of data, Data in Excel
    """
    import openpyxl
    
    # Load the workbook
    workbook = openpyxl.load_workbook(file_name)
    
    # Get the active sheet
    sheet = workbook.active
    
    # Read all data from the sheet
    data = []
    for row in sheet.iter_rows(values_only=True):
        data.append(list(row))
    
    # Close the workbook
    workbook.close()
    
    return data