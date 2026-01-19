def create_table(self, table_name, key1, key2):
    """
    Crea una nuova tabella nel database se non esiste.
    E imposta id (INTEGER) come CHIAVE PRIMARIA, imposta key1 come TEXT, key2 come INTEGER
    :param table_name: str, il nome della tabella da creare.
    :param key1: str, il nome della prima colonna nella tabella.
    :param key2: str, il nome della seconda colonna nella tabella.
    >>> db.create_table('user', 'name', 'age')
    """
    query = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        id INTEGER PRIMARY KEY,
        {key1} TEXT,
        {key2} INTEGER
    )
    """
    self.cursor.execute(query)
    self.conn.commit()