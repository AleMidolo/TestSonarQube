def read_excel(self, file_name):
    """
    从Excel文件读取数据
    :param file_name:str, 要读取的Excel文件名
    :return:list of data, Excel中的数据
    """
    import openpyxl
    
    # 加载工作簿
    workbook = openpyxl.load_workbook(file_name)
    
    # 获取活动工作表
    sheet = workbook.active
    
    # 读取所有数据
    data = []
    for row in sheet.iter_rows(values_only=True):
        data.append(list(row))
    
    # 关闭工作簿
    workbook.close()
    
    return data