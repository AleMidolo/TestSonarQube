def create_table(self, table_name, key1, key2):
    """
    如果数据库中不存在，则创建一个新表。
    并将 id (INTEGER) 设为主键，将 key1 设为 TEXT，将 key2 设为 INTEGER
    :param table_name: str, 要创建的表的名称。
    :param key1: str, 表中第一列的名称。
    :param key2: str, 表中第二列的名称。
    >>> db.create_table('user', 'name', 'age')
    """
    query = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        id INTEGER PRIMARY KEY,
        {key1} TEXT,
        {key2} INTEGER
    )
    """
    self.cursor.execute(query)
    self.conn.commit()