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
    set_clause = ', '.join((f"{k}='{v}'" for k, v in data.items()))
    query = f'UPDATE {table} SET {set_clause}'
    if where:
        query += ' WHERE ' + ' AND '.join((f"{k}='{v}'" for k, v in where.items()))
    return query