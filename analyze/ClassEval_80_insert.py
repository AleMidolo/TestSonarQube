@staticmethod
def insert(table, data):
    """
    Generate the INSERT SQL statement from the given parameters.
    :param table: str, the table to be inserted in database.
    :param data: dict, the key and value in SQL insert statement
    :return query: str, the SQL insert statement.
    >>> SQLQueryBuilder.insert('table1', {'name': 'Test', 'age': 14})
    "INSERT INTO table1 (name, age) VALUES ('Test', '14')"
    """
    columns = ', '.join(data.keys())
    values = ', '.join(f"'{value}'" for value in data.values())
    query = f"INSERT INTO {table} ({columns}) VALUES ({values})"
    return query