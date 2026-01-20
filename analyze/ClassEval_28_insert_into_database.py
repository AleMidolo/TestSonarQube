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
    
    # Crear la parte de columnas de la consulta SQL
    columns_str = ', '.join(columns)
    
    # Crear placeholders para los valores
    placeholders = ', '.join(['?' for _ in columns])
    
    # Construir la consulta SQL
    query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders})"
    
    # Preparar los valores para cada fila
    values_list = []
    for row in data:
        values = [row.get(col) for col in columns]
        values_list.append(tuple(values))
    
    # Ejecutar la inserción (asumiendo que self tiene una conexión de base de datos)
    cursor = self.connection.cursor()
    cursor.executemany(query, values_list)
    self.connection.commit()