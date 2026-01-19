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
    # Convert snake_case key to camelCase
    def to_camel_case(snake_str):
        components = snake_str.split('_')
        return components[0] + ''.join(x.title() for x in components[1:])
    
    camel_key = to_camel_case(key)
    
    # Try to get the value using the camelCase key from the internal dictionary
    if hasattr(self, '_data'):
        return self._data[camel_key]
    else:
        # If _data doesn't exist, try to access as a regular dict
        return super().__getitem__(camel_key)