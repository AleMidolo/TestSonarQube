def process_excel_data(self, N, save_file_name):
    """
    将Excel文件中指定列的内容转换为大写
    :param N: int, 要更改的列的序号
    :param save_file_name: str, 源文件名
    :return:(int, str), 前者是write_excel的返回值，而后者是处理后数据的保存文件名
    >>> processor = ExcelProcessor()
    >>> success, output_file = processor.process_excel_data(1, 'test_data.xlsx')
    """
    import openpyxl
    import os
    
    # 读取Excel文件
    workbook = openpyxl.load_workbook(save_file_name)
    sheet = workbook.active
    
    # 将指定列(N)的内容转换为大写
    # N是列序号,从1开始
    for row in sheet.iter_rows(min_row=1, min_col=N, max_col=N):
        for cell in row:
            if cell.value is not None and isinstance(cell.value, str):
                cell.value = cell.value.upper()
    
    # 生成输出文件名
    base_name, ext = os.path.splitext(save_file_name)
    output_file_name = f"{base_name}_processed{ext}"
    
    # 保存修改后的文件
    workbook.save(output_file_name)
    workbook.close()
    
    # 调用write_excel方法(假设该方法存在于self中)
    result = self.write_excel(output_file_name)
    
    return (result, output_file_name)