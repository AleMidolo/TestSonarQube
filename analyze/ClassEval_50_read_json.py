def read_json(self, file_path):
    """
        एक JSON फ़ाइल पढ़ें और डेटा लौटाएँ।
        :param file_path: str, JSON फ़ाइल का पथ।
        :return: dict, यदि पढ़ने की प्रक्रिया के दौरान कोई त्रुटि नहीं होती है तो JSON फ़ाइल से डेटा, या -1 लौटाएँ यदि पढ़ने की प्रक्रिया के दौरान कोई त्रुटि होती है।
                    यदि फ़ाइल मौजूद नहीं है तो 0 लौटाएँ।
        >>> json.read_json('test.json')
        {'name': 'test', 'age': 14}
        """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return 0
    except:
        return -1