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
    if not data:
        return
    conn = sqlite3.connect(self.database_name)
    cursor = conn.cursor()
    columns = list(data[0].keys())
    placeholders = ', '.join(['?'] * len(columns))
    column_names = ', '.join(columns)
    insert_query = f'INSERT INTO {table_name} ({column_names}) VALUES ({placeholders})'
    values_list = [tuple((row[col] for col in columns)) for row in data]
    cursor.executemany(insert_query, values_list)
    conn.commit()
    conn.close()