def read_excel(self, file_name):
    """
        Leyendo datos de archivos de Excel
        :param file_name:str, nombre del archivo de Excel a leer
        :return:list de datos, Datos en Excel
        """
    try:
        workbook = openpyxl.load_workbook(file_name, data_only=True)
        sheet = workbook.active
        data = []
        for row in sheet.iter_rows(values_only=True):
            data.append(row)
        workbook.close()
        return data
    except:
        return None