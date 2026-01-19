def read_csv(self, file_name):
    """
    通过 file_name 读取csv文件,从中获取标题和数据
    :param file_name: str, csv文件的名称
    :return title, data: (list, list), 第一行是标题,其余是数据
    >>> csvProcessor = CSVProcessor()
    >>> csvProcessor.read_csv('read_test.csv')
    (['a', 'b', 'c', 'd'], [['hElLo', 'YoU', 'ME', 'LoW']])
    """
    import csv
    
    title = []
    data = []
    
    with open(file_name, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        
        # 读取第一行作为标题
        title = next(csv_reader)
        
        # 读取剩余行作为数据
        for row in csv_reader:
            data.append(row)
    
    return title, data