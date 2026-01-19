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
    for row in data:
        name = row.get('name')
        age = row.get('age')
        insert_query = f'INSERT INTO {table_name} (name, age) VALUES (?, ?)'
        cursor.execute(insert_query, (name, age))
    conn.commit()
    conn.close()