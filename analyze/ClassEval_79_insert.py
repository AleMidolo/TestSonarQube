def insert(self, data):
    """
    दिए गए डेटा के आधार पर एक INSERT SQL कथन उत्पन्न करता है।
    :param data: dict. डेटा जो डिक्शनरी रूप में डाला जाएगा जहाँ कुंजी फ़ील्ड नाम हैं और मान फ़ील्ड मान हैं।
    :return: str. उत्पन्न SQL कथन।
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
            formatted_values.append(f"'{value}'")
        elif value is None:
            formatted_values.append('NULL')
        else:
            formatted_values.append(str(value))
    
    values = ', '.join(formatted_values)
    
    # Assuming self has a table_name attribute (e.g., self.table_name = 'table1')
    table_name = getattr(self, 'table_name', 'table1')
    
    # Generate INSERT statement
    sql_statement = f"INSERT INTO {table_name} ({columns}) VALUES ({values});"
    
    return sql_statement