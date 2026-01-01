@staticmethod
def delete(table, where=None):
    """
        Genera la declaración SQL DELETE a partir de los parámetros dados.
        :param table: str, la tabla que se ejecutará con la operación DELETE en la base de datos
        :param where: dict, {key1: value1, key2: value2 ...}. La condición de la consulta.
        :return query: str, la declaración SQL de eliminación.
        >>> SQLQueryBuilder.delete('table1', {'name': 'Test', 'age': 14})
        "DELETE FROM table1 WHERE name='Test' AND age='14'"
        """
    query = f'DELETE FROM {table}'
    if where:
        query += ' WHERE ' + ' AND '.join((f"{k}='{v}'" for k, v in where.items()))
    return query