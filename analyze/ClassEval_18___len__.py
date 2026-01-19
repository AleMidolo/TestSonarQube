def __len__(self):
    """
    Devuelve la longitud de los datos propios
    :return:int, longitud de los datos
    >>> camelize_map = CamelCaseMap()
    >>> camelize_map['first_name'] = 'John'
    >>> camelize_map['last_name'] = 'Doe'
    >>> camelize_map['age'] = 30
    >>> camelize_map.__len__()
    3
    """
    return len(self.__dict__)