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
    set_clause = ', '.join((f"{k}='{v}'" for k, v in data.items()))
    query = f'UPDATE {table} SET {set_clause}'
    if where:
        query += ' WHERE ' + ' AND '.join((f"{k}='{v}'" for k, v in where.items()))
    return query