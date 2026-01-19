def select(table, columns='*', where=None):
    """
    从给定参数生成 SELECT SQL 语句。
    :param table: str，数据库中要查询的表。
    :param columns: list of str，['col1', 'col2']。
    :param where: dict，{key1: value1, key2: value2 ...}。查询条件。
    return query: str，SQL 查询语句。
    >>> SQLQueryBuilder.select('table1', columns = ["col1","col2"], where = {"age": 15})
    "SELECT col1, col2 FROM table1 WHERE age='15'"
    """
    # Handle columns
    if columns == '*':
        columns_str = '*'
    elif isinstance(columns, list):
        columns_str = ', '.join(columns)
    else:
        columns_str = columns
    
    # Build base query
    query = f"SELECT {columns_str} FROM {table}"
    
    # Handle WHERE clause
    if where:
        conditions = []
        for key, value in where.items():
            conditions.append(f"{key}='{value}'")
        where_clause = ' AND '.join(conditions)
        query += f" WHERE {where_clause}"
    
    return query