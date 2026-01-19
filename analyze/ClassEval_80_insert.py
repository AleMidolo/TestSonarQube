@staticmethod
def insert(table, data):
    """
    दिए गए पैरामीटर से INSERT SQL कथन उत्पन्न करें।
    :param table: str, डेटाबेस में डाले जाने वाला तालिका।
    :param data: dict, SQL INSERT कथन में कुंजी और मान
    :return query: str, SQL INSERT कथन।
    >>> SQLQueryBuilder.insert('table1', {'name': 'Test', 'age': 14})
    "INSERT INTO table1 (name, age) VALUES ('Test', '14')"
    """
    columns = ', '.join(data.keys())
    values = ', '.join(f"'{value}'" for value in data.values())
    query = f"INSERT INTO {table} ({columns}) VALUES ({values})"
    return query