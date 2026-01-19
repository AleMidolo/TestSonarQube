def select(table, columns='*', where=None):
    """
    दिए गए पैरामीटर से SELECT SQL कथन उत्पन्न करें।
    :param table: str, डेटाबेस में क्वेरी तालिका।
    :param columns: str की सूची, ['col1', 'col2']।
    :param where: dict, {key1: value1, key2: value2 ...}. क्वेरी की शर्त।
    return query: str, SQL क्वेरी कथन।
    >>> SQLQueryBuilder.select('table1', columns = ["col1","col2"], where = {"age": 15})
    "SELECT col1, col2 FROM table1 WHERE age='15'"
    """
    # Handle columns parameter
    if columns == '*':
        columns_str = '*'
    elif isinstance(columns, list):
        columns_str = ', '.join(columns)
    else:
        columns_str = columns
    
    # Build base query
    query = f"SELECT {columns_str} FROM {table}"
    
    # Handle where clause
    if where is not None and isinstance(where, dict) and len(where) > 0:
        where_clauses = []
        for key, value in where.items():
            where_clauses.append(f"{key}='{value}'")
        where_str = ' AND '.join(where_clauses)
        query += f" WHERE {where_str}"
    
    return query