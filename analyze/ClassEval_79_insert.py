def insert(self, data):
    """
    Generates an INSERT SQL statement based on the given data.
    :param data: dict. The data to be inserted, in dictionary form where keys are field names and values are field values.
    :return: str. The generated SQL statement.
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
        else:
            formatted_values.append(str(value))
    
    values = ', '.join(formatted_values)
    
    # Assuming self has a table_name attribute based on the example
    table_name = getattr(self, 'table_name', 'table1')
    
    return f"INSERT INTO {table_name} ({columns}) VALUES ({values});"