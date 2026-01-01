def get_argument(self, key):
    """
        निर्दिष्ट तर्क का मान तर्कों की शब्दकोश से प्राप्त करता है और इसे लौटाता है।
        :param key: str, तर्क का नाम
        :return: तर्क का मान, या None यदि तर्क मौजूद नहीं है।
        >>> parser.arguments
        {'arg1': 'value1', 'arg2': 'value2', 'option1': True, 'option2': True}
        >>> parser.get_argument('arg2')
        'value2'
        """
    return self.arguments.get(key)