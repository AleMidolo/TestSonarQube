def create_table(self):
    """
    如果数据库中尚不存在，则创建一个"tickets"表。字段包括类型为int的ID，类型为str的电影名称，类型为str的剧院名称，类型为str的座位号，以及类型为str的顾客名称。
    :return: None
    """
    cursor = self.conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY,
            movie_name TEXT NOT NULL,
            theater_name TEXT NOT NULL,
            seat_number TEXT NOT NULL,
            customer_name TEXT NOT NULL
        )
    ''')
    self.conn.commit()