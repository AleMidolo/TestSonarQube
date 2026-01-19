def create_table(self, table_name, key1, key2):
    """
        Create a new table in the database if it doesn't exist.
        And make id (INTEGER) as PRIMARY KEY, make key1 as TEXT, key2 as INTEGER
        :param table_name: str, the name of the table to create.
        :param key1: str, the name of the first column in the table.
        :param key2: str, the name of the second column in the table.
        >>> db.create_table('user', 'name', 'age')
        """
    conn = sqlite3.connect(self.database_name)
    cursor = conn.cursor()
    create_table_query = f'\n        CREATE TABLE IF NOT EXISTS {table_name} (\n            id INTEGER PRIMARY KEY AUTOINCREMENT,\n            {key1} TEXT,\n            {key2} INTEGER\n        )\n        '
    cursor.execute(create_table_query)
    conn.commit()
    conn.close()