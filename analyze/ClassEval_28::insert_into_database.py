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
    conn = sqlite3.connect(self.database_name)
    cursor = conn.cursor()
    if data and len(data) > 0:
        columns = list(data[0].keys())
        placeholders = ', '.join(['?'] * len(columns))
        column_names = ', '.join(columns)
        insert_query = f'INSERT INTO {table_name} ({column_names}) VALUES ({placeholders})'
        values_list = [tuple((row[col] for col in columns)) for row in data]
        cursor.executemany(insert_query, values_list)
        conn.commit()
    conn.close()