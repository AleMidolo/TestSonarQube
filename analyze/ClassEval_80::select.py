@staticmethod
def select(table, columns='*', where=None):
    """
        Genera l'istruzione SQL SELECT dai parametri forniti.
        :param table: str, la tabella di query nel database.
        :param columns: lista di str, ['col1', 'col2'].
        :param where: dict, {key1: value1, key2: value2 ...}. La condizione di query.
        return query: str, l'istruzione di query SQL.
        >>> SQLQueryBuilder.select('table1', columns = ["col1","col2"], where = {"age": 15})
        "SELECT col1, col2 FROM table1 WHERE age='15'"
        """
    columns_str = ', '.join(columns) if isinstance(columns, list) else columns
    query = f'SELECT {columns_str} FROM {table}'
    if where:
        query += ' WHERE ' + ' AND '.join((f"{k}='{v}'" for k, v in where.items()))
    return query