def insert_ticket(self, movie_name, theater_name, seat_number, customer_name):
    """
    Inserisce un nuovo biglietto nella tabella "tickets".
    :param movie_name: str, il nome del film.
    :param theater_name: str, il nome del teatro.
    :param seat_number: str, il numero del posto.
    :param customer_name: str, il nome del cliente.
    :return: None
    """
    query = """
    INSERT INTO tickets (movie_name, theater_name, seat_number, customer_name)
    VALUES (?, ?, ?, ?)
    """
    self.cursor.execute(query, (movie_name, theater_name, seat_number, customer_name))
    self.conn.commit()