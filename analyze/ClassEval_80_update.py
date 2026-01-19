@staticmethod
def update(table, data, where=None):
    """
        从给定的参数生成 UPDATE SQL 语句。
        :param table: str，将在数据库中执行 UPDATE 操作的表
        :param data: dict，SQL 更新语句中的键和值
        :param where: dict，{key1: value1, key2: value2 ...}。查询条件。
        >>> SQLQueryBuilder.update('table1', {'name': 'Test2', 'age': 15}, where = {'name':'Test'})
        "UPDATE table1 SET name='Test2', age='15' WHERE name='Test'"
        """
    set_clause = ', '.join((f"{k}='{v}'" for k, v in data.items()))
    query = f'UPDATE {table} SET {set_clause}'
    if where:
        query += ' WHERE ' + ' AND '.join((f"{k}='{v}'" for k, v in where.items()))
    return query