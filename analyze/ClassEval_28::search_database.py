def search_database(self, table_name, name):
    """
        Search the specified table in the database for rows with a matching name.
        :param table_name: str, the name of the table to search.
        :param name: str, the name to search for.
        :return: list, a list of tuples representing the rows with matching name, if any;
                    otherwise, returns None.
        >>> db.search_database('user', 'John')
        [(1, 'John', 25)]
        """
    conn = sqlite3.connect(self.database_name)
    cursor = conn.cursor()
    cursor.execute(f'PRAGMA table_info({table_name})')
    columns_info = cursor.fetchall()
    name_column = None
    for col_info in columns_info:
        if col_info[2] == 'TEXT':
            name_column = col_info[1]
            break
    result = None
    if name_column:
        search_query = f'SELECT * FROM {table_name} WHERE {name_column} = ?'
        cursor.execute(search_query, (name,))
        result = cursor.fetchall()
    conn.close()
    return result if result else None