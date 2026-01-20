def select(self, fields=None, condition=None):
    """
    Genera una declaración SQL SELECT basada en los campos y condiciones especificados.
    :param fields: lista, opcional. El valor predeterminado es None. La lista de campos a consultar.
    :param condition: str, opcional. El valor predeterminado es None. La expresión de condición para la consulta.
    :return: str. La declaración SQL generada.
    >>> sql = SQLGenerator('table1')
    >>> sql.select(['field1', 'field2'], 'filed3 = value1')
    'SELECT field1, field2 FROM table1 WHERE filed3 = value1;'
    """
    if fields is None:
        fields_str = '*'
    else:
        fields_str = ', '.join(fields)
    
    sql = f'SELECT {fields_str} FROM {self.table_name}'
    
    if condition is not None:
        sql += f' WHERE {condition}'
    
    sql += ';'
    
    return sql