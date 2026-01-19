@staticmethod
def delete(table, where=None):
    """
    Genera l'istruzione SQL DELETE dai parametri forniti.
    :param table: str, la tabella che verrà eseguita con l'operazione DELETE nel database
    :param where: dict, {key1: value1, key2: value2 ...}. La condizione della query.
    :return query: str, l'istruzione SQL delete.
    >>> SQLQueryBuilder.delete('table1', {'name': 'Test', 'age': 14})
    "DELETE FROM table1 WHERE name='Test' AND age='14'"
    """
    query = f"DELETE FROM {table}"
    
    if where:
        conditions = []
        for key, value in where.items():
            conditions.append(f"{key}='{value}'")
        query += " WHERE " + " AND ".join(conditions)
    
    return query