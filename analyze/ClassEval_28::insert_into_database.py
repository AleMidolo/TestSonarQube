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
    if not data:
        return
    conn = sqlite3.connect(self.database_name)
    cursor = conn.cursor()
    columns = list(data[0].keys())
    placeholders = ', '.join(['?' for _ in columns])
    column_names = ', '.join(columns)
    insert_query = f'INSERT INTO {table_name} ({column_names}) VALUES ({placeholders})'
    values_list = [tuple((item[col] for col in columns)) for item in data]
    cursor.executemany(insert_query, values_list)
    conn.commit()
    conn.close()