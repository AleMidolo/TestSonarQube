def select(self, fields=None, condition=None):
    """
    Genera un'istruzione SQL SELECT basata sui campi e le condizioni specificati.
    :param fields: lista, opzionale. Il valore predefinito è None. La lista dei campi da interrogare.
    :param condition: str, opzionale. Il valore predefinito è None. L'espressione di condizione per l'interrogazione.
    :return: str. L'istruzione SQL generata.
    >>> sql = SQLGenerator('table1')
    >>> sql.select(['field1', 'field2'], 'filed3 = value1')
    'SELECT field1, field2 FROM table1 WHERE filed3 = value1;'
    """
    if fields is None:
        fields_str = '*'
    else:
        fields_str = ', '.join(fields)
    
    sql = f'SELECT {fields_str} FROM {self.table_name}'
    
    if condition:
        sql += f' WHERE {condition}'
    
    sql += ';'
    
    return sql