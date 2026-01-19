def insert_ticket(self, movie_name, theater_name, seat_number, customer_name):
    """
    "tickets" तालिका में एक नया टिकट डालता है।
    :param movie_name: str, फिल्म का नाम।
    :param theater_name: str, थिएटर का नाम।
    :param seat_number: str, सीट नंबर।
    :param customer_name: str, ग्राहक का नाम।
    :return: None
    """
    query = """
    INSERT INTO tickets (movie_name, theater_name, seat_number, customer_name)
    VALUES (?, ?, ?, ?)
    """
    self.cursor.execute(query, (movie_name, theater_name, seat_number, customer_name))
    self.conn.commit()