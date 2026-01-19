def read_excel(self, file_name):
    """
    Leyendo datos de archivos de Excel
    :param file_name:str, nombre del archivo de Excel a leer
    :return:list de datos, Datos en Excel
    """
    import openpyxl
    
    # Cargar el archivo de Excel
    workbook = openpyxl.load_workbook(file_name)
    
    # Obtener la hoja activa
    sheet = workbook.active
    
    # Leer todos los datos de la hoja
    data = []
    for row in sheet.iter_rows(values_only=True):
        data.append(list(row))
    
    # Cerrar el workbook
    workbook.close()
    
    return data