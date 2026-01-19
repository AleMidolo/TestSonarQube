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
    text_column = None
    for col_info in columns_info:
        if col_info[2] == 'TEXT':
            text_column = col_info[1]
            break
    if text_column:
        delete_query = f'DELETE FROM {table_name} WHERE {text_column} = ?'
        cursor.execute(delete_query, (name,))
    else:
        print(f'No TEXT column found in table {table_name}')
    conn.commit()
    conn.close()