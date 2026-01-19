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
    
    # 获取列名（从第一条数据中）
    columns = list(data[0].keys())
    column_names = ', '.join(columns)
    placeholders = ', '.join(['?' for _ in columns])
    
    # 构建 INSERT SQL 语句
    sql = f"INSERT INTO {table_name} ({column_names}) VALUES ({placeholders})"
    
    # 准备要插入的值
    values_list = []
    for row in data:
        values = tuple(row[col] for col in columns)
        values_list.append(values)
    
    # 执行批量插入
    cursor = self.connection.cursor()
    cursor.executemany(sql, values_list)
    self.connection.commit()