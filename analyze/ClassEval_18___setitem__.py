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
    def snake_to_camel(snake_str):
        components = snake_str.split('_')
        # Keep the first component as is, capitalize the rest
        return components[0] + ''.join(x.title() for x in components[1:])
    
    camel_key = snake_to_camel(key)
    # Store using the camelCase key in the underlying dictionary
    super().__setitem__(camel_key, value)