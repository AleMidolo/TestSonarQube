def __delitem__(self, key):
    """
    की से जुड़ी वैल्यू डिलीट करें।

    :param key: str
    :return: None

    >>> camelize_map = CamelCaseMap()
    >>> camelize_map['first_name'] = 'John'
    >>> camelize_map.__delitem__('first_name')
    >>> flag = 'first_name' in camelize_map
    >>> flag
    False
    """
    # Convert snake_case key to camelCase
    camel_key = self._to_camel_case(key)
    
    # Delete the item using the camelCase key from the internal dictionary
    del self._data[camel_key]