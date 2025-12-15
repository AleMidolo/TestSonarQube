def insert_into_database(self, table_name, data):
        """
        将数据插入到数据库中指定的表。
        :param table_name: str, 要插入数据的表的名称。
        :param data: list, 一个字典列表，其中每个字典代表一行数据。
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