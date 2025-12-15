def process_json(self, file_path, remove_key):
    """
    एक JSON फ़ाइल पढ़ें और निर्दिष्ट कुंजी को हटाकर डेटा को संसाधित करें और संशोधित डेटा को फ़ाइल में फिर से लिखें।

    :param file_path: str, JSON फ़ाइल का पथ।
    :param remove_key: str, हटाई जाने वाली कुंजी।
    :return: 1, यदि निर्दिष्ट कुंजी सफलतापूर्वक हटा दी गई है और डेटा को फिर से लिखा गया है।
                0, यदि फ़ाइल मौजूद नहीं है या निर्दिष्ट कुंजी डेटा में मौजूद नहीं है.
    >>> json.read_json('test.json')
    {'key1': 'value1', 'key2': 'value2'}
    >>> json.process_json('test.json', 'key1')
    1
    >>> json.read_json('test.json')
    {'key2': 'value2'}
    """
    
    data = self.read_json(file_path)
    if data == 0 or remove_key not in data:
        return 0
    
    del data[remove_key]
    self.write_json(data, file_path)
    return 1