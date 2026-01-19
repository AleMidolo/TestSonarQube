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
    import csv
    import os
    
    try:
        # 读取CSV文件
        title, data = self.read_csv(save_file_name)
        
        # 检查N是否在有效范围内
        if N < 0 or N >= len(title):
            return 0
        
        # 仅保留第N列的标题
        new_title = [title[N]]
        
        # 仅保留第N列的数据并将其大写
        new_data = []
        for row in data:
            if N < len(row):
                new_data.append([row[N].upper()])
        
        # 生成新文件名：在扩展名前添加'_process'
        base_name, ext = os.path.splitext(save_file_name)
        new_file_name = base_name + '_process' + ext
        
        # 写入新的CSV文件
        with open(new_file_name, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(new_title)
            writer.writerows(new_data)
        
        return 1
    except Exception as e:
        return 0