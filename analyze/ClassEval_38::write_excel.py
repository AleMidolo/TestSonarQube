def write_excel(self, data, file_name):
    """
        Escribir datos en el archivo de Excel especificado
        :param data: list, Datos a ser escritos
        :param file_name: str, Nombre del archivo de Excel en el que se escribirá
        :return: 0 o 1, 1 representa escritura exitosa, 0 representa escritura fallida
        >>> processor = ExcelProcessor()
        >>> new_data = [
        >>>     ('Nombre', 'Edad', 'País'),
        >>>     ('John', 25, 'EE.UU.'),
        >>>     ('Alice', 30, 'Canadá'),
        >>>     ('Bob', 35, 'Australia'),
        >>>     ('Julia', 28, 'Alemania')
        >>> ]
        >>> data = processor.write_excel(new_data, 'test_data.xlsx')
        """
    try:
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        for row_idx, row in enumerate(data, start=1):
            for col_idx, value in enumerate(row, start=1):
                sheet.cell(row=row_idx, column=col_idx, value=value)
        workbook.save(file_name)
        workbook.close()
        return 1
    except:
        return 0