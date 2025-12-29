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
    for row in data:
        name = row.get('name')
        age = row.get('age')
        insert_query = f'INSERT INTO {table_name} (name, age) VALUES (?, ?)'
        cursor.execute(insert_query, (name, age))
    conn.commit()
    conn.close()