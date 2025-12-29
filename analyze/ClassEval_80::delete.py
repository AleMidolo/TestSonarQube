@staticmethod
def delete(table, where=None):
    """
        从给定参数生成 DELETE SQL 语句。
        :param table: str，将在数据库中执行 DELETE 操作的表
        :param where: dict, {key1: value1, key2: value2 ...}。查询条件。
        :return query: str, SQL 删除语句。
        >>> SQLQueryBuilder.delete('table1', {'name': 'Test', 'age': 14})
        "DELETE FROM table1 WHERE name='Test' AND age='14'"
        """
    query = f'DELETE FROM {table}'
    if where:
        query += ' WHERE ' + ' AND '.join((f"{k}='{v}'" for k, v in where.items()))
    return query