def __iter__(self):
    """
    अपने डेटा के साथ इटरेबल ऑब्जेक्ट्स लौटाना
    :return:Iterator
    >>> camelize_map = CamelCaseMap()
    >>> camelize_map['first_name'] = 'John'
    >>> camelize_map['last_name'] = 'Doe'
    >>> camelize_map['age'] = 30
    >>> camelize_map.__iter__()
    <dict_keyiterator object at 0x0000026739977C20>
    """
    return iter(self.data)