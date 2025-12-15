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
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        
        for entry in data:
            insert_query = f"INSERT INTO {table_name} ({', '.join(entry.keys())}) VALUES ({', '.join(['?' for _ in entry.values()])})"
            cursor.execute(insert_query, tuple(entry.values()))
        
        conn.commit()
        conn.close()