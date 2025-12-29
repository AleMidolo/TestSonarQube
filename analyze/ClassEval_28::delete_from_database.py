def delete_from_database(self, table_name, name):
    """
        Elimina righe dalla tabella indicata del database con un nome corrispondente.
        :param table_name: str, il nome della tabella da cui eliminare le righe.
        :param name: str, il nome da abbinare per l'eliminazione.
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
    if name_column is None:
        conn.close()
        return
    delete_query = f'DELETE FROM {table_name} WHERE {name_column} = ?'
    cursor.execute(delete_query, (name,))
    conn.commit()
    conn.close()