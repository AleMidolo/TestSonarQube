def insert_into_database(self, table_name, data):
    """
    Inserta datos en la tabla especificada en la base de datos.
    :param table_name: str, el nombre de la tabla en la que se insertarán los datos.
    :param data: list, una lista de diccionarios donde cada diccionario representa una fila de datos.
    >>> db.insert_into_database('user', [
            {'name': 'John', 'age': 25},
            {'name': 'Alice', 'age': 30}
        ])
    """
    if not data:
        return
    
    # Get column names from the first dictionary
    columns = list(data[0].keys())
    column_names = ', '.join(columns)
    placeholders = ', '.join(['?' for _ in columns])
    
    # Prepare the SQL INSERT statement
    sql = f"INSERT INTO {table_name} ({column_names}) VALUES ({placeholders})"
    
    # Prepare the values for each row
    values_list = []
    for row in data:
        values = tuple(row[col] for col in columns)
        values_list.append(values)
    
    # Execute the insert operation
    cursor = self.connection.cursor()
    cursor.executemany(sql, values_list)
    self.connection.commit()