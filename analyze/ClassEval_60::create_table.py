def create_table(self):
    """
    Creates the "tickets" table if it does not already exist. 
    The table includes fields for an integer ID, a string for the movie name, 
    a string for the theater name, a string for the seat number, 
    and a string for the customer name.
    :return: None
    """
    self.cursor.execute('\n            CREATE TABLE IF NOT EXISTS tickets (\n                id INTEGER PRIMARY KEY AUTOINCREMENT,\n                movie_name TEXT NOT NULL,\n                theater_name TEXT NOT NULL,\n                seat_number TEXT NOT NULL,\n                customer_name TEXT NOT NULL\n            )\n        ')
    self.connection.commit()