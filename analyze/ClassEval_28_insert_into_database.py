def insert_into_database(self, table_name, data):
    """
    Insert data into the specified table in the database.
    :param table_name: str, the name of the table to insert data into.
    :param data: list, a list of dictionaries where each dictionary represents a row of data.
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
    
    # Extract values from each dictionary in the same order as columns
    values_list = []
    for row in data:
        values = [row[col] for col in columns]
        values_list.append(tuple(values))
    
    # Execute the insert statement
    cursor = self.connection.cursor()
    cursor.executemany(sql, values_list)
    self.connection.commit()