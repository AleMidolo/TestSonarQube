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
    # Build SET clause
    set_parts = []
    for key, value in data.items():
        set_parts.append(f"{key}='{value}'")
    set_clause = ", ".join(set_parts)
    
    # Build the base UPDATE statement
    sql = f"UPDATE {table} SET {set_clause}"
    
    # Add WHERE clause if provided
    if where:
        where_parts = []
        for key, value in where.items():
            where_parts.append(f"{key}='{value}'")
        where_clause = " AND ".join(where_parts)
        sql += f" WHERE {where_clause}"
    
    return sql