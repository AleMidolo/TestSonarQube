def read_excel(self, file_name):
    """
        从Excel文件读取数据
        :param file_name:str, 要读取的Excel文件名
        :return:list of data, Excel中的数据
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