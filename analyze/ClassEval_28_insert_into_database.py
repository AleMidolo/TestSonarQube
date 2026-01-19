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
    
    # Get column names from the first dictionary
    columns = list(data[0].keys())
    column_names = ', '.join(columns)
    placeholders = ', '.join(['?' for _ in columns])
    
    # Prepare the SQL INSERT statement
    sql = f"INSERT INTO {table_name} ({column_names}) VALUES ({placeholders})"
    
    # Prepare the values for each row
    values_list = []
    for row in data:
        values = tuple(row[col] for col in columns)
        values_list.append(values)
    
    # Execute the insert operation
    cursor = self.connection.cursor()
    cursor.executemany(sql, values_list)
    self.connection.commit()