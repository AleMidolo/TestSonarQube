def write_excel(self, data, file_name):
    """
        将数据写入指定的Excel文件
        :param data: list, 要写入的数据
        :param file_name: str, 要写入的Excel文件名
        :return: 0或1, 1表示写入成功，0表示写入失败
        >>> processor = ExcelProcessor()
        >>> new_data = [
        >>>     ('姓名', '年龄', '国家'),
        >>>     ('约翰', 25, '美国'),
        >>>     ('爱丽丝', 30, '加拿大'),
        >>>     ('鲍勃', 35, '澳大利亚'),
        >>>     ('朱莉亚', 28, '德国')
        >>> ]
        >>> data = processor.write_excel(new_data, 'test_data.xlsx')
        """
    try:
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        for row in data:
            sheet.append(row)
        workbook.save(file_name)
        workbook.close()
        return 1
    except:
        return 0