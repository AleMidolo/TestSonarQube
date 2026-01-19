@staticmethod
def update(table, data, where=None):
    """
        Genera la declaración SQL UPDATE a partir de los parámetros dados.
        :param table: str, la tabla que se ejecutará con la operación UPDATE en la base de datos
        :param data: dict, la clave y el valor en la declaración SQL de actualización
        :param where: dict, {key1: value1, key2: value2 ...}. La condición de la consulta.
        >>> SQLQueryBuilder.update('table1', {'name': 'Test2', 'age': 15}, where = {'name':'Test'})
        "UPDATE table1 SET name='Test2', age='15' WHERE name='Test'"
        """
    set_clause = ', '.join((f"{k}='{v}'" for k, v in data.items()))
    query = f'UPDATE {table} SET {set_clause}'
    if where:
        query += ' WHERE ' + ' AND '.join((f"{k}='{v}'" for k, v in where.items()))
    return query