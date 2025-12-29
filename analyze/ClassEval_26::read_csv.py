def read_csv(self, file_name):
    """
        csv फ़ाइल को file_name द्वारा पढ़ें, शीर्षक और डेटा प्राप्त करें
        :param file_name: str, csv फ़ाइल का नाम
        :return title, data: (list, list), पहली पंक्ति शीर्षक है, बाकी डेटा है
        >>> csvProcessor = CSVProcessor()
        >>> csvProcessor.read_csv('read_test.csv')
        (['a', 'b', 'c', 'd'], [['hElLo', 'YoU', 'ME', 'LoW']])
        """
    try:
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            title = next(reader)
            data = [row for row in reader]
        return (title, data)
    except:
        return ([], [])