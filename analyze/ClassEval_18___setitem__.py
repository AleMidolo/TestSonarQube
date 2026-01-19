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
    # Convert snake_case key to camelCase
    def to_camel_case(snake_str):
        components = snake_str.split('_')
        return components[0] + ''.join(x.title() for x in components[1:])
    
    camel_key = to_camel_case(key)
    super().__setitem__(camel_key, value)