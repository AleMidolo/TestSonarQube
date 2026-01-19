import csv

def read_csv(self, file_name):
    """
    通过 file_name 读取csv文件，从中获取标题和数据
    :param file_name: str, csv文件的名称
    :return title, data: (list, list), 第一行是标题，其余是数据
    >>> csvProcessor = CSVProcessor()
    >>> csvProcessor.read_csv('read_test.csv')
    (['a', 'b', 'c', 'd'], [['hElLo', 'YoU', 'ME', 'LoW']])
    """
    with open(file_name, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
        
        if len(rows) == 0:
            return [], []
        
        title = rows[0]
        data = rows[1:]
        
        return title, data