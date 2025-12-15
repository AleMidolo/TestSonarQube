def create_table(self):
        """
        Creates the "tickets" table if it does not already exist. The table includes fields for an ID of type int, 
        movie_name of type str, theater_name of type str, seat_number of type str, and customer_name of type str.
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