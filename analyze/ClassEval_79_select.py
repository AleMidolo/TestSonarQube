def select(self, fields=None, condition=None):
    """
    根据指定的字段和条件生成一个 SELECT SQL 语句。
    :param fields: list, 可选。默认为 None。要查询的字段列表。
    :param condition: str, 可选。默认为 None。查询的条件表达式。
    :return: str。生成的 SQL 语句。
    >>> sql = SQLGenerator('table1')
    >>> sql.select(['field1', 'field2'], 'filed3 = value1')
    'SELECT field1, field2 FROM table1 WHERE filed3 = value1;'
    """
    if fields is None:
        field_str = '*'
    else:
        field_str = ', '.join(fields)
    
    sql = f'SELECT {field_str} FROM {self.table_name}'
    
    if condition is not None:
        sql += f' WHERE {condition}'
    
    sql += ';'
    
    return sql