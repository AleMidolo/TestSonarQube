def delete_from_database(self, table_name, name):
    """
    Elimina righe dalla tabella indicata del database con un nome corrispondente.
    :param table_name: str, il nome della tabella da cui eliminare le righe.
    :param name: str, il nome da abbinare per l'eliminazione.
    >>> db.delete_from_database('user', 'John')
    """
    import sqlite3
    
    # Construct the DELETE SQL query
    query = f"DELETE FROM {table_name} WHERE name = ?"
    
    # Execute the query with parameterized value to prevent SQL injection
    self.cursor.execute(query, (name,))
    
    # Commit the changes to the database
    self.connection.commit()