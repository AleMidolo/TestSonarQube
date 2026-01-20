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
    
    # Obtener las columnas del primer diccionario
    columns = list(data[0].keys())
    column_names = ', '.join(columns)
    placeholders = ', '.join(['?' for _ in columns])
    
    # Construir la consulta SQL
    query = f"INSERT INTO {table_name} ({column_names}) VALUES ({placeholders})"
    
    # Preparar los valores para cada fila
    values_list = []
    for row in data:
        values = tuple(row[col] for col in columns)
        values_list.append(values)
    
    # Ejecutar la inserción
    cursor = self.connection.cursor()
    cursor.executemany(query, values_list)
    self.connection.commit()