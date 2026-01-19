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
        import csv
        
        # Read the CSV file
        result = self.read_csv(save_file_name)
        if result is None:
            return 0
        
        title, data = result
        
        # Check if N is valid
        if N < 0 or N >= len(title):
            return 0
        
        # Process data: keep only Nth column and capitalize
        new_data = []
        for row in data:
            if N < len(row):
                new_data.append([row[N].upper()])
            else:
                return 0
        
        # Generate new file name with '_process' suffix
        if save_file_name.endswith('.csv'):
            new_file_name = save_file_name[:-4] + '_process.csv'
        else:
            new_file_name = save_file_name + '_process'
        
        # Write to new CSV file
        with open(new_file_name, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(title)
            writer.writerows(new_data)
        
        return 1
    except:
        return 0