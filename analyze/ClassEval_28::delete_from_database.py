def delete_from_database(self, table_name, name):
    """
        Delete rows from the specified table in the database with a matching name.
        :param table_name: str, the name of the table to delete rows from.
        :param name: str, the name to match for deletion.
        >>> db.delete_from_database('user', 'John')
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
    if name_column is not None:
        delete_query = f'DELETE FROM {table_name} WHERE {name_column} = ?'
        cursor.execute(delete_query, (name,))
    conn.commit()
    conn.close()