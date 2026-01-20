def write_excel(self, data, file_name):
    """
    Escribir datos en el archivo de Excel especificado
    :param data: list, Datos a ser escritos
    :param file_name: str, Nombre del archivo de Excel en el que se escribirá
    :return: 0 o 1, 1 representa escritura exitosa, 0 representa escritura fallida
    """
    try:
        import openpyxl
        from openpyxl import Workbook
        
        # Crear un nuevo libro de trabajo
        wb = Workbook()
        ws = wb.active
        
        # Escribir los datos en la hoja de cálculo
        for row in data:
            ws.append(row)
        
        # Guardar el archivo
        wb.save(file_name)
        
        return 1
    except Exception as e:
        return 0