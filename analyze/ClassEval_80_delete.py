@staticmethod
def delete(table, where=None):
    """
    दिए गए पैरामीटर से DELETE SQL कथन उत्पन्न करें।
    :param table: str, वह तालिका जिस पर DELETE ऑपरेशन डेटाबेस में निष्पादित किया जाएगा
    :param where: dict, {key1: value1, key2: value2 ...}. क्वेरी की शर्त।
    :return query: str, SQL delete कथन।
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