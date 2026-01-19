def read_csv(self, file_name):
    """
        通过 file_name 读取csv文件，从中获取标题和数据
        :param file_name: str, csv文件的名称
        :return title, data: (list, list), 第一行是标题，其余是数据
        >>> csvProcessor = CSVProcessor()
        >>> csvProcessor.read_csv('read_test.csv')
        (['a', 'b', 'c', 'd'], [['hElLo', 'YoU', 'ME', 'LoW']])
        """
    try:
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            title = next(reader)
            data = [row for row in reader]
        return (title, data)
    except:
        return ([], [])