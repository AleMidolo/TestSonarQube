def insert_into_database(self, table_name, data):
        """
        Inserisce i dati nella tabella indicata del database..
        :param table_name: str, il nome della tabella in cui inserire i dati.
        :param data: list, un elenco di dizionari dove ogni dizionario rappresenta una riga di dati.
        >>> db.insert_into_database('user', [
                {'name': 'John', 'age': 25},
                {'name': 'Alice', 'age': 30}
            ])
        """
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        for entry in data:
            insert_query = f"INSERT INTO {table_name} ({', '.join(entry.keys())}) VALUES ({', '.join(['?' for _ in entry.values()])})"
            cursor.execute(insert_query, tuple(entry.values()))

        conn.commit()
        conn.close()