def read_csv(self, file_name):
    """
    Read the csv file by file_name, get the title and data from it
    :param file_name: str, name of the csv file
    :return title, data: (list, list), first row is title, the rest is data
    >>> csvProcessor = CSVProcessor()
    >>> csvProcessor.read_csv('read_test.csv')
    (['a', 'b', 'c', 'd'], [['hElLo', 'YoU', 'ME', 'LoW']])
    """
    import csv
    
    with open(file_name, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        rows = list(csv_reader)
        
        if len(rows) == 0:
            return [], []
        
        title = rows[0]
        data = rows[1:]
        
        return title, data