def __getitem__(self, key):
    """
        की से जुड़ी वैल्यू लौटाएँ।

        :param key: str
        :return: str, की से जुड़ी वैल्यू

        >>> camelize_map = CamelCaseMap()
        >>> camelize_map['first_name'] = 'John'
        >>> camelize_map.__getitem__('first_name')
        'John'
        """
    return self._data[self._convert_key(key)]