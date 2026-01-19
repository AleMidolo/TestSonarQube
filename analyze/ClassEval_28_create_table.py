def create_table(self, table_name, key1, key2):
    """
        Crea una nueva tabla en la base de datos si no existe.
        Y hace que id (INTEGER) sea la CLAVE PRIMARIA, hace que key1 sea TEXT, key2 sea INTEGER
        :param table_name: str, el nombre de la tabla a crear.
        :param key1: str, el nombre de la primera columna en la tabla.
        :param key2: str, el nombre de la segunda columna en la tabla.
        >>> db.create_table('user', 'name', 'age')
        """
    conn = sqlite3.connect(self.database_name)
    cursor = conn.cursor()
    create_table_query = f'\n        CREATE TABLE IF NOT EXISTS {table_name} (\n            id INTEGER PRIMARY KEY,\n            {key1} TEXT,\n            {key2} INTEGER\n        )\n        '
    cursor.execute(create_table_query)
    conn.commit()
    conn.close()