def create_table(self):
    """
    Creates a "tickets" table in the database if it does not exist already.Fields include ID of type int, movie name of type str, theater name of type str, seat number of type str, and customer name of type str
    :return: None
    """
    cursor = self.conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tickets (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            movie_name TEXT NOT NULL,
            theater_name TEXT NOT NULL,
            seat_number TEXT NOT NULL,
            customer_name TEXT NOT NULL
        )
    ''')
    self.conn.commit()