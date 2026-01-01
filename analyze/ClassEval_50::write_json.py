def write_json(self, data, file_path):
    """
        डेटा को JSON फ़ाइल में लिखें और इसे दिए गए पथ पर सहेजें।

        :param data: dict, JSON फ़ाइल में लिखे जाने वाले डेटा।
        :param file_path: str, JSON फ़ाइल का पथ।
        :return: 1 यदि लेखन प्रक्रिया सफल होती है, या -1, यदि लेखन प्रक्रिया के दौरान कोई त्रुटि होती है।
        >>> json.write_json({'key1': 'value1', 'key2': 'value2'}, 'test.json')
        1
        >>> json.read_json('test.json')
        {'key1': 'value1', 'key2': 'value2'}
        """
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        return 1
    except:
        return -1