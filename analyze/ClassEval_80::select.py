@staticmethod
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
    columns_str = ', '.join(columns) if isinstance(columns, list) else columns
    query = f'SELECT {columns_str} FROM {table}'
    if where:
        query += ' WHERE ' + ' AND '.join((f"{k}='{v}'" for k, v in where.items()))
    return query