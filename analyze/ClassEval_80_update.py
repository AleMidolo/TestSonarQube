@staticmethod
def update(table, data, where=None):
    """
    Generate the UPDATE SQL statement from the given parameters.
    :param table: str, the table that will be excuted with UPDATE operation in database
    :param data: dict, the key and value in SQL update statement
    :param where: dict, {key1: value1, key2: value2 ...}. The query condition.
    >>> SQLQueryBuilder.update('table1', {'name': 'Test2', 'age': 15}, where = {'name':'Test'})
    "UPDATE table1 SET name='Test2', age='15' WHERE name='Test'"
    """
    set_clause = ', '.join([f"{key}='{value}'" for key, value in data.items()])
    sql = f"UPDATE {table} SET {set_clause}"
    
    if where:
        where_clause = ' AND '.join([f"{key}='{value}'" for key, value in where.items()])
        sql += f" WHERE {where_clause}"
    
    return sql