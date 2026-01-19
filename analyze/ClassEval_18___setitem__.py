def __setitem__(self, key, value):
    """
        कुंजी के लिए संबंधित मान को निर्दिष्ट मान पर सेट करें
        :param key:str
        :param value:str, निर्दिष्ट मान
        :return:None
        >>> camelize_map = CamelCaseMap()
        >>> camelize_map['first_name'] = 'John'
        >>> camelize_map.__setitem__('first_name', 'new name')
        camelize_map['first_name'] = 'new name'
        """
    self._data[self._convert_key(key)] = value