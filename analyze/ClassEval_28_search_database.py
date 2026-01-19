def search_database(self, table_name, name):
    """
    Cerca nella tabella indicata del database righe con un nome corrispondente.
    :param table_name: str, il nome della tabella da cercare.
    :param name: str, il nome da cercare.
    :return: list, una lista di tuple che rappresentano le righe con nome corrispondente, se presenti;
                altrimenti, restituisce None.
    >>> db.search_database('user', 'John')
    [(1, 'John', 25)]
    """
    try:
        cursor = self.connection.cursor()
        query = f"SELECT * FROM {table_name} WHERE name = ?"
        cursor.execute(query, (name,))
        results = cursor.fetchall()
        
        if results:
            return results
        else:
            return None
    except Exception as e:
        return None