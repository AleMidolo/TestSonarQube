def search_database(self, table_name, name):
    """
        Busca en la tabla especificada en la base de datos filas con un nombre coincidente.
        :param table_name: str, el nombre de la tabla a buscar.
        :param name: str, el nombre a buscar.
        :return: list, una lista de tuplas que representan las filas con el nombre coincidente, si las hay;
                    de lo contrario, devuelve None.
        >>> db.search_database('user', 'John')
        [(1, 'John', 25)]
        """
    conn = sqlite3.connect(self.database_name)
    cursor = conn.cursor()
    search_query = f'SELECT * FROM {table_name} WHERE name = ?'
    cursor.execute(search_query, (name,))
    results = cursor.fetchall()
    conn.close()
    return results if results else None