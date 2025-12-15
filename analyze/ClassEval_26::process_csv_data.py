def process_csv_data(self, N, save_file_name):
    """
    Read a csv file into variable title and data.
    Only remain the N th (from 0) column data and Capitalize them, store the title and new data into a new csv file.
    Add '_process' suffix after old file name, as a new file name.
    :param N: int, the N th column(from 0)
    :param save_file_name, the name of file that needs to be processed.
    :return:int, if success return 1, or 0 otherwise
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
        new_data = [[row[N].upper()] for row in data if len(row) > N]
        new_file_name = save_file_name.replace('.csv', '_process.csv')
        self.write_csv([title], new_file_name)
        self.write_csv(new_data, new_file_name)
        return 1
    except Exception as e:
        return 0