def create_table(self, table_name, key1, key2):
    """
        如果数据库中不存在，则创建一个新表。
        并将 id (INTEGER) 设为主键，将 key1 设为 TEXT，将 key2 设为 INTEGER
        :param table_name: str, 要创建的表的名称。
        :param key1: str, 表中第一列的名称。
        :param key2: str, 表中第二列的名称。
        >>> db.create_table('user', 'name', 'age')
        """
    conn = sqlite3.connect(self.database_name)
    cursor = conn.cursor()
    create_query = f'\n        CREATE TABLE IF NOT EXISTS {table_name} (\n            id INTEGER PRIMARY KEY AUTOINCREMENT,\n            {key1} TEXT,\n            {key2} INTEGER\n        )\n        '
    cursor.execute(create_query)
    conn.commit()
    conn.close()