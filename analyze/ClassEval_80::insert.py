@staticmethod
def insert(table, data):
    """
        Genera la declaración SQL INSERT a partir de los parámetros dados.
        :param table: str, la tabla en la que se va a insertar en la base de datos.
        :param data: dict, la clave y el valor en la declaración SQL de inserción.
        :return query: str, la declaración SQL de inserción.
        >>> SQLQueryBuilder.insert('table1', {'name': 'Test', 'age': 14})
        "INSERT INTO table1 (name, age) VALUES ('Test', '14')"
        """
    columns = ', '.join(data.keys())
    values = ', '.join((f"'{v}'" for v in data.values()))
    return f'INSERT INTO {table} ({columns}) VALUES ({values})'