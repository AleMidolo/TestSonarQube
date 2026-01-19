@staticmethod
def insert(table, data):
    """
        从给定参数生成 INSERT SQL 语句。
        :param table: str，要插入的数据库表。
        :param data: dict，SQL 插入语句中的键和值
        :return query: str，SQL 插入语句。
        >>> SQLQueryBuilder.insert('table1', {'name': 'Test', 'age': 14})
        "INSERT INTO table1 (name, age) VALUES ('Test', '14')"
        """
    columns = ', '.join(data.keys())
    values = ', '.join((f"'{v}'" for v in data.values()))
    return f'INSERT INTO {table} ({columns}) VALUES ({values})'