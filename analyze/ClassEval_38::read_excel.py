def read_excel(self, file_name):
    """
        Lettura dei dati dai file Excel
        :param file_name:str, nome del file Excel da leggere
        :return:list di dati, Dati in Excel
        """
    try:
        workbook = openpyxl.load_workbook(file_name)
        sheet = workbook.active
        data = []
        for row in sheet.iter_rows(values_only=True):
            data.append(row)
        workbook.close()
        return data
    except:
        return None