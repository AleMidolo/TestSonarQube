def select(table, columns='*', where=None):
    """
    Genera la declaración SQL SELECT a partir de los parámetros dados.
    :param table: str, la tabla de consulta en la base de datos.
    :param columns: lista de str, ['col1', 'col2'].
    :param where: dict, {key1: value1, key2: value2 ...}. La condición de consulta.
    return query: str, la declaración de consulta SQL.
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
    if where is not None and len(where) > 0:
        conditions = []
        for key, value in where.items():
            conditions.append(f"{key}='{value}'")
        where_clause = ' AND '.join(conditions)
        query += f" WHERE {where_clause}"
    
    return query