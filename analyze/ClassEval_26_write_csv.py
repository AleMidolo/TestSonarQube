def write_csv(self, data, file_name):
    """
    डेटा को एक csv फ़ाइल में लिखें।
    :param file_name: str, csv फ़ाइल का नाम
    :return:int, यदि सफल हो तो 1 लौटाएं, अन्यथा 0
    >>> csvProcessor = CSVProcessor()
    >>> csvProcessor.write_csv([['a', 'b', 'c', 'd'], ['1', '2', '3', '4']], 'write_test.csv')
    1
    """
    import csv
    
    try:
        with open(file_name, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        return 1
    except:
        return 0