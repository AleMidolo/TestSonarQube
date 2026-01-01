def create_table(self):
    """
    Creates the "tickets" table if it does not already exist. 
    The table includes fields for an ID of type int, movie_name of type str, 
    theater_name of type str, seat_number of type str, and customer_name of type str.
    :return: None
    """
    self.cursor.execute('\n        CREATE TABLE IF NOT EXISTS tickets (\n            id INTEGER PRIMARY KEY AUTOINCREMENT,\n            movie_name TEXT NOT NULL,\n            theater_name TEXT NOT NULL,\n            seat_number TEXT NOT NULL,\n            customer_name TEXT NOT NULL\n        )\n    ')
    self.connection.commit()