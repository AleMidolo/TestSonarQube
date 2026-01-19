def insert_ticket(self, movie_name, theater_name, seat_number, customer_name):
    """
    Inserta un nuevo ticket en la tabla "tickets".
    :param movie_name: str, el nombre de la película.
    :param theater_name: str, el nombre del teatro.
    :param seat_number: str, el número de asiento.
    :param customer_name: str, el nombre del cliente.
    :return: None
    """
    query = """
    INSERT INTO tickets (movie_name, theater_name, seat_number, customer_name)
    VALUES (?, ?, ?, ?)
    """
    self.cursor.execute(query, (movie_name, theater_name, seat_number, customer_name))
    self.conn.commit()