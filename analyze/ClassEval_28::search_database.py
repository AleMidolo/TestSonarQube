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
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        search_query = f"SELECT * FROM {table_name} WHERE name = ?"
        cursor.execute(search_query, (name,))
        results = cursor.fetchall()

        conn.close()
        return results if results else None