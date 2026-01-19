def delete_from_database(self, table_name, name):
    """
    Elimina righe dalla tabella indicata del database con un nome corrispondente.
    :param table_name: str, il nome della tabella da cui eliminare le righe.
    :param name: str, il nome da abbinare per l'eliminazione.
    >>> db.delete_from_database('user', 'John')
    """
    import sqlite3
    
    # Sanitize table name to prevent SQL injection
    # Note: table names cannot be parameterized, so we validate it
    if not table_name.replace('_', '').isalnum():
        raise ValueError("Invalid table name")
    
    # Connect to database (assuming self has a connection or database path)
    if hasattr(self, 'connection'):
        conn = self.connection
        should_close = False
    elif hasattr(self, 'db_path'):
        conn = sqlite3.connect(self.db_path)
        should_close = True
    else:
        raise AttributeError("Database connection or path not found")
    
    try:
        cursor = conn.cursor()
        
        # Use parameterized query for the name value to prevent SQL injection
        query = f"DELETE FROM {table_name} WHERE name = ?"
        cursor.execute(query, (name,))
        
        conn.commit()
    finally:
        if should_close:
            conn.close()