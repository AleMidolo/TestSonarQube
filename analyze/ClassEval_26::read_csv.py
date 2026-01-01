def read_csv(self, file_name):
    """
        Read the csv file by file_name, get the title and data from it
        :param file_name: str, name of the csv file
        :return title, data: (list, list), first row is title, the rest is data
        >>> csvProcessor = CSVProcessor()
        >>> csvProcessor.read_csv('read_test.csv')
        (['a', 'b', 'c', 'd'], [['hElLo', 'YoU', 'ME', 'LoW']])
        """
    try:
        with open(file_name, 'r', newline='') as file:
            reader = csv.reader(file)
            title = next(reader)
            data = [row for row in reader]
        return (title, data)
    except:
        return ([], [])