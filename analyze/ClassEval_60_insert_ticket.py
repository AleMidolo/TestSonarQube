def insert_ticket(self, movie_name, theater_name, seat_number, customer_name):
    """
    将新票插入到"tickets"表中。
    :param movie_name: str，电影名称。
    :param theater_name: str，剧院名称。
    :param seat_number: str，座位号。
    :param customer_name: str，顾客名称。
    :return: None
    """
    cursor = self.conn.cursor()
    cursor.execute(
        "INSERT INTO tickets (movie_name, theater_name, seat_number, customer_name) VALUES (?, ?, ?, ?)",
        (movie_name, theater_name, seat_number, customer_name)
    )
    self.conn.commit()