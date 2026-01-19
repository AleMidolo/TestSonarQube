@staticmethod
def update(table, data, where=None):
    """
    Genera l'istruzione SQL UPDATE dai parametri forniti.
    :param table: str, la tabella che verrà eseguita con l'operazione UPDATE nel database
    :param data: dict, la chiave e il valore nell'istruzione SQL di aggiornamento
    :param where: dict, {key1: value1, key2: value2 ...}. La condizione della query.
    >>> SQLQueryBuilder.update('table1', {'name': 'Test2', 'age': 15}, where = {'name':'Test'})
    "UPDATE table1 SET name='Test2', age='15' WHERE name='Test'"
    """
    # Build the SET clause
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