def insert_ticket(self, movie_name, theater_name, seat_number, customer_name):
    """
    Inserts a new ticket into the "tickets" table.
    :param movie_name: str, the name of the movie.
    :param theater_name: str, the name of the theater.
    :param seat_number: str, the seat number.
    :param customer_name: str, the name of the customer.
    :return: None
    """
    query = """
    INSERT INTO tickets (movie_name, theater_name, seat_number, customer_name)
    VALUES (?, ?, ?, ?)
    """
    self.cursor.execute(query, (movie_name, theater_name, seat_number, customer_name))
    self.connection.commit()