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
    for entry in data:
        insert_query = f"INSERT INTO {table_name} ({', '.join(entry.keys())}) VALUES ({', '.join(['?' for _ in entry.values()])})"
        cursor.execute(insert_query, tuple(entry.values()))
    conn.commit()
    conn.close()