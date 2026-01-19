def write_excel(self, data, file_name):
    """
    Scrivi i dati nel file Excel specificato
    :param data: list, Dati da scrivere
    :param file_name: str, Nome del file Excel in cui scrivere
    :return: 0 o 1, 1 rappresenta una scrittura riuscita, 0 rappresenta una scrittura fallita
    >>> processor = ExcelProcessor()
    >>> new_data = [
    >>>     ('Nome', 'Età', 'Paese'),
    >>>     ('John', 25, 'USA'),
    >>>     ('Alice', 30, 'Canada'),
    >>>     ('Bob', 35, 'Australia'),
    >>>     ('Julia', 28, 'Germania')
    >>> ]
    >>> data = processor.write_excel(new_data, 'test_data.xlsx')
    """
    try:
        import openpyxl
        
        # Crea un nuovo workbook
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        
        # Scrivi i dati nel foglio
        for row_data in data:
            sheet.append(row_data)
        
        # Salva il file
        workbook.save(file_name)
        
        return 1
    except Exception as e:
        return 0