def create_table(self):
    """
        Crea una tabla "tickets" en la base de datos si no existe ya. Los campos incluyen ID de tipo int, nombre de la película de tipo str, nombre del teatro de tipo str, número de asiento de tipo str y nombre del cliente de tipo str.
        :return: None
        """
    self.cursor.execute('\n            CREATE TABLE IF NOT EXISTS tickets (\n                id INTEGER PRIMARY KEY AUTOINCREMENT,\n                movie_name TEXT NOT NULL,\n                theater_name TEXT NOT NULL,\n                seat_number TEXT NOT NULL,\n                customer_name TEXT NOT NULL\n            )\n        ')
    self.connection.commit()