def create_table(self):
    """
    Creates the "tickets" table if it does not already exist. 
    The table includes fields for an integer ID, a string for the movie name, 
    a string for the theater name, a string for the seat number, 
    and a string for the customer name.
    :return: None
    """
    self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tickets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                movie_name TEXT NOT NULL,
                theater_name TEXT NOT NULL,
                seat_number TEXT NOT NULL,
                customer_name TEXT NOT NULL
            )
        ''')
    self.connection.commit()