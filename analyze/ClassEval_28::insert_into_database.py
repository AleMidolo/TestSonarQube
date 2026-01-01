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
    cursor.execute(f'PRAGMA table_info({table_name})')
    columns_info = cursor.fetchall()
    column_names = [col[1] for col in columns_info if col[1] != 'id']
    placeholders = ', '.join(['?' for _ in column_names])
    column_names_str = ', '.join(column_names)
    insert_query = f'INSERT INTO {table_name} ({column_names_str}) VALUES ({placeholders})'
    for row in data:
        values = [row.get(col) for col in column_names]
        cursor.execute(insert_query, values)
    conn.commit()
    conn.close()