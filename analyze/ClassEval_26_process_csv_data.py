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
    import csv
    import os
    
    try:
        # Read the CSV file
        with open(save_file_name, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            rows = list(reader)
        
        if not rows:
            return 0
        
        # Extract title (header row)
        title = rows[0]
        
        # Check if N is valid
        if N < 0 or N >= len(title):
            return 0
        
        # Process data rows - keep only Nth column and capitalize
        processed_data = []
        for row in rows[1:]:
            if N < len(row):
                processed_data.append([row[N].upper()])
        
        # Create new file name with '_process' suffix
        base_name, ext = os.path.splitext(save_file_name)
        new_file_name = base_name + '_process' + ext
        
        # Write to new CSV file
        with open(new_file_name, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(title)  # Write original title
            writer.writerows(processed_data)  # Write processed data
        
        return 1
    
    except Exception as e:
        return 0