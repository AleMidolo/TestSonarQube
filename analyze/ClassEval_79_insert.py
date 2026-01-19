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
    
    # Format values - wrap strings in single quotes
    formatted_values = []
    for value in data.values():
        if isinstance(value, str):
            # Escape single quotes in strings
            escaped_value = value.replace("'", "''")
            formatted_values.append(f"'{escaped_value}'")
        elif value is None:
            formatted_values.append('NULL')
        elif isinstance(value, bool):
            formatted_values.append('TRUE' if value else 'FALSE')
        else:
            formatted_values.append(str(value))
    
    values = ', '.join(formatted_values)
    
    # Assuming self has a table_name attribute
    table_name = getattr(self, 'table_name', 'table1')
    
    return f"INSERT INTO {table_name} ({columns}) VALUES ({values});"