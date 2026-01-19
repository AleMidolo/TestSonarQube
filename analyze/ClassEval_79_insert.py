def insert(self, data):
    """
    根据给定的数据生成一个 INSERT SQL 语句。
    :param data: dict. 要插入的数据，以字典形式表示，其中键是字段名，值是字段值。
    :return: str. 生成的 SQL 语句。
    >>> sql.insert({'key1': 'value1', 'key2': 'value2'})
    "INSERT INTO table1 (key1, key2) VALUES ('value1', 'value2');"
    """
    if not data:
        return ""
    
    # Extract column names and values
    columns = ', '.join(data.keys())
    values = ', '.join(f"'{value}'" if isinstance(value, str) else str(value) for value in data.values())
    
    # Assuming self has a table_name attribute based on the example
    table_name = getattr(self, 'table_name', 'table1')
    
    # Generate the INSERT statement
    sql_statement = f"INSERT INTO {table_name} ({columns}) VALUES ({values});"
    
    return sql_statement