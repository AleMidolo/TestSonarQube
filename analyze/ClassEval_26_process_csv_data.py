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
        new_data = []
        for row in data:
            if N < len(row):
                new_data.append([row[N].upper()])
            else:
                new_data.append([''])
        if '.' in save_file_name:
            name_parts = save_file_name.rsplit('.', 1)
            new_file_name = f'{name_parts[0]}_process.{name_parts[1]}'
        else:
            new_file_name = f'{save_file_name}_process'
        filtered_title = [title[N]] if N < len(title) else ['']
        data_to_write = [filtered_title] + new_data
        return self.write_csv(data_to_write, new_file_name)
    except:
        return 0