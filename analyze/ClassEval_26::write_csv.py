def write_csv(self, data, file_name):
    """
        将数据写入csv文件。
        :param file_name: str, csv文件的名称
        :return:int, 如果成功返回1，否则返回0
        >>> csvProcessor = CSVProcessor()
        >>> csvProcessor.write_csv([['a', 'b', 'c', 'd'], ['1', '2', '3', '4']], 'write_test.csv')
        1
        """
    try:
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        return 1
    except Exception:
        return 0