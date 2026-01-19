def process_csv_data(self, N, save_file_name):
    """
    एक CSV फ़ाइल को टाइटल और डेटा वेरिएबल में पढ़ें।
    डेटा का सिर्फ़ Nवां कॉलम (0 से) रखें और उन्हें कैपिटलाइज़ करें।
    टाइटल और नए डेटा को एक नई CSV फ़ाइल में स्टोर करें।
    पुराने फ़ाइलनेम में '_process' सफ़िक्स जोड़कर नई फ़ाइल बनाएं।

    :param N: int, Nवां कॉलम (0 से)
    :param save_file_name: प्रोसेस करने वाली फ़ाइल का नाम
    :return: int, सफल हो तो 1 लौटाएँ, नहीं तो 0

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
        
        # Create new filename with '_process' suffix
        base_name, ext = os.path.splitext(save_file_name)
        new_file_name = base_name + '_process' + ext
        
        # Write to new CSV file
        with open(new_file_name, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(title)
            writer.writerows(new_data)
        
        return 1
    except Exception as e:
        return 0