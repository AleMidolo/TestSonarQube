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
        return (0, '')
    processed_data = []
    for row in data:
        new_row = list(row)
        if N >= 0 and N < len(new_row):
            cell_value = new_row[N]
            if isinstance(cell_value, str):
                new_row[N] = cell_value.upper()
        processed_data.append(tuple(new_row))
    output_file = f'processed_{save_file_name}'
    result = self.write_excel(processed_data, output_file)
    return (result, output_file)