def __len__(self):
    """
        Restituisce la lunghezza dei propri dati
        :return:int, lunghezza dei dati
        >>> camelize_map = CamelCaseMap()
        >>> camelize_map['first_name'] = 'John'
        >>> camelize_map['last_name'] = 'Doe'
        >>> camelize_map['age'] = 30
        >>> camelize_map.__len__()
        3
        """
    return len(self._data)