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
    search_query = f'SELECT * FROM {table_name} WHERE name = ?'
    cursor.execute(search_query, (name,))
    results = cursor.fetchall()
    conn.close()
    if results:
        return results
    else:
        return None