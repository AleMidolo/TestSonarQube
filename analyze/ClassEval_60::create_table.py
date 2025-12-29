def create_table(self):
    """
        Creates a "tickets" table in the database if it does not already exist. 
        The fields include ID of type int, movie name of type str, theater name of type str, 
        seat number of type str, and customer name of type str.
        :return: None
        """
    self.cursor.execute('\n            CREATE TABLE IF NOT EXISTS tickets (\n                id INTEGER PRIMARY KEY AUTOINCREMENT,\n                movie_name TEXT NOT NULL,\n                theater_name TEXT NOT NULL,\n                seat_number TEXT NOT NULL,\n                customer_name TEXT NOT NULL\n            )\n        ')
    self.connection.commit()