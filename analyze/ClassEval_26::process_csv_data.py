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
    try:
        title, data = self.read_csv(save_file_name)
        processed_data = []
        for row in data:
            if N < len(row):
                processed_row = [row[N].upper()]
                processed_data.append(processed_row)
            else:
                processed_data.append([''])
        base_name = save_file_name.rsplit('.', 1)[0]
        extension = save_file_name.rsplit('.', 1)[1] if '.' in save_file_name else 'csv'
        new_file_name = f'{base_name}_process.{extension}'
        if N < len(title):
            new_title = [title[N]]
        else:
            new_title = ['']
        write_data = [new_title] + processed_data
        return self.write_csv(write_data, new_file_name)
    except Exception as e:
        return 0