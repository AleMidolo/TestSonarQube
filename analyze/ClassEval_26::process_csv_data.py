def process_csv_data(self, N, save_file_name):
    """
        读取一个csv文件到变量title和data中。
        仅保留第N列（从0开始）的数据并将其大写，将标题和新数据存储到一个新的csv文件中。
        在旧文件名后添加'_process'后缀，作为新文件名。
        :param N: int，第N列（从0开始）
        :param save_file_name: 需要处理的文件名。
        :return: int，如果成功返回1，否则返回0
        >>> csvProcessor = CSVProcessor()
        >>> csvProcessor.read_csv('read_test.csv')
        (['a', 'b', 'c', 'd'], [['hElLo', 'YoU', 'ME', 'LoW']])
        >>> csvProcessor.process_csv_data(0, 'read_test.csv')
        1
        >>> csvProcessor.read_csv('read_test_process.csv')
        (['a', 'b', 'c', 'd'], [['HELLO']])
        """
    try:
        title, data = self.read_csv(save_file_name)
        if N < 0 or N >= len(title):
            return 0
        new_data = []
        for row in data:
            if N < len(row):
                new_data.append([row[N].upper()])
            else:
                new_data.append([''])
        base_name = save_file_name.rsplit('.', 1)[0]
        extension = save_file_name.rsplit('.', 1)[1] if '.' in save_file_name else 'csv'
        new_file_name = f'{base_name}_process.{extension}'
        write_data = [[title[N]]] + new_data
        return self.write_csv(write_data, new_file_name)
    except Exception:
        return 0