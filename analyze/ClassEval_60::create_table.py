def create_table(self):
    """
        Creates a "tickets" table in the database if it does not already exist.
        The table includes fields for an integer ID, string movie name, string theater name, string seat number, and string customer name.
        :return: None
        """
    self.cursor.execute('\n            CREATE TABLE IF NOT EXISTS tickets (\n                id INTEGER PRIMARY KEY AUTOINCREMENT,\n                movie_name TEXT NOT NULL,\n                theater_name TEXT NOT NULL,\n                seat_number TEXT NOT NULL,\n                customer_name TEXT NOT NULL\n            )\n        ')
    self.connection.commit()