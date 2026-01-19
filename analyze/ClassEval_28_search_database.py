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
    try:
        cursor = self.connection.cursor()
        query = f"SELECT * FROM {table_name} WHERE name = ?"
        cursor.execute(query, (name,))
        results = cursor.fetchall()
        
        if results:
            return results
        else:
            return None
    except Exception as e:
        return None