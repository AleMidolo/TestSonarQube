def create_table(self):
    """
        Creates a "tickets" table if it does not exist in the database.
        The table includes fields for an ID (int), movie name (str), theater name (str), seat number (str), and customer name (str).
        :return: None
        """
    self.cursor.execute('\n            CREATE TABLE IF NOT EXISTS tickets (\n                id INTEGER PRIMARY KEY AUTOINCREMENT,\n                movie_name TEXT NOT NULL,\n                theater_name TEXT NOT NULL,\n                seat_number TEXT NOT NULL,\n                customer_name TEXT NOT NULL\n            )\n        ')
    self.connection.commit()