def select(self, fields=None, condition=None):
    """
        Generates a SELECT SQL statement based on the specified fields and conditions.
        :param fields: list, optional. Default is None. The list of fields to be queried.
        :param condition: str, optional. Default is None. The condition expression for the query.
        :return: str. The generated SQL statement.
        >>> sql = SQLGenerator('table1')
        >>> sql.select(['field1', 'field2'], 'filed3 = value1')
        'SELECT field1, field2 FROM table1 WHERE filed3 = value1;'
        """
    if fields is None:
        fields_clause = '*'
    else:
        fields_clause = ', '.join(fields)
    sql = f'SELECT {fields_clause} FROM {self.table_name}'
    if condition:
        sql += f' WHERE {condition}'
    return sql + ';'