def process_excel_data(self, N, save_file_name):
    """
    将Excel文件中指定列的内容转换为大写
    :param N: int, 要更改的列的序号
    :param save_file_name: str, 源文件名
    :return:(int, str), 前者是write_excel的返回值，而后者是处理后数据的保存文件名
    >>> processor = ExcelProcessor()
    >>> success, output_file = processor.process_excel_data(1, 'test_data.xlsx')
    """
    data = self.read_excel(save_file_name)
    if data is None:
        return (0, save_file_name)
    for i in range(len(data)):
        if len(data[i]) > N:
            data[i] = list(data[i])
            data[i][N] = data[i][N].upper()
    output_file_name = 'processed_' + save_file_name
    success = self.write_excel(data, output_file_name)
    return (success, output_file_name)