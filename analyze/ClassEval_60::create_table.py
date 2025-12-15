def create_table(self):
        """
        Creates a "tickets" table in the database if it does not already exist.
        The table includes fields for an integer ID, string movie name, string theater name, string seat number, and string customer name.
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