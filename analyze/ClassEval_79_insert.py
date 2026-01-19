def insert(self, data):
    """
    Genera un'istruzione SQL INSERT basata sui dati forniti.
    :param data: dict. I dati da inserire, in forma di dizionario dove le chiavi sono i nomi dei campi e i valori sono i valori dei campi.
    :return: str. L'istruzione SQL generata.
    >>> sql.insert({'key1': 'value1', 'key2': 'value2'})
    "INSERT INTO table1 (key1, key2) VALUES ('value1', 'value2');"
    """
    if not data:
        return ""
    
    # Extract column names and values
    columns = ', '.join(data.keys())
    values = ', '.join(f"'{value}'" for value in data.values())
    
    # Generate the INSERT statement
    sql_statement = f"INSERT INTO {self.table_name} ({columns}) VALUES ({values});"
    
    return sql_statement