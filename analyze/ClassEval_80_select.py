def select(table, columns='*', where=None):
    """
    Genera l'istruzione SQL SELECT dai parametri forniti.
    :param table: str, la tabella di query nel database.
    :param columns: lista di str, ['col1', 'col2'].
    :param where: dict, {key1: value1, key2: value2 ...}. La condizione di query.
    return query: str, l'istruzione di query SQL.
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