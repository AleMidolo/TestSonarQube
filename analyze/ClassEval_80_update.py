@staticmethod
def update(table, data, where=None):
    """
    दिए गए पैरामीटर से UPDATE SQL कथन उत्पन्न करें।
    :param table: str, वह तालिका जिस पर डेटाबेस में UPDATE ऑपरेशन किया जाएगा
    :param data: dict, SQL अपडेट कथन में कुंजी और मान
    :param where: dict, {key1: value1, key2: value2 ...}. क्वेरी की शर्त।
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