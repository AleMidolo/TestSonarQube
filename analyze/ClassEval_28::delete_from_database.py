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
    text_column = None
    for col in columns_info:
        if col[2] == 'TEXT':
            text_column = col[1]
            break
    if text_column is None:
        conn.close()
        return
    delete_query = f'DELETE FROM {table_name} WHERE {text_column} = ?'
    cursor.execute(delete_query, (name,))
    conn.commit()
    conn.close()