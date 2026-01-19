@staticmethod
def insert(table, data):
    """
    Genera l'istruzione SQL INSERT dai parametri forniti.
    :param table: str, la tabella in cui inserire nel database.
    :param data: dict, la chiave e il valore nell'istruzione SQL di inserimento
    :return query: str, l'istruzione SQL di inserimento.
    >>> SQLQueryBuilder.insert('table1', {'name': 'Test', 'age': 14})
    "INSERT INTO table1 (name, age) VALUES ('Test', '14')"
    """
    columns = ', '.join(data.keys())
    values = ', '.join(f"'{value}'" for value in data.values())
    query = f"INSERT INTO {table} ({columns}) VALUES ({values})"
    return query