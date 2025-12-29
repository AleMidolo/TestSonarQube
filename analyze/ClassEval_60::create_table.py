def create_table(self):
    """
        Crea una tabella "tickets" nel database se non esiste già. I campi includono ID di tipo int, nome del film di tipo str, nome del teatro di tipo str, numero del posto di tipo str e nome del cliente di tipo str.
        :return: None
        """
    self.cursor.execute('\n            CREATE TABLE IF NOT EXISTS tickets (\n                id INTEGER PRIMARY KEY AUTOINCREMENT,\n                movie_name TEXT NOT NULL,\n                theater_name TEXT NOT NULL,\n                seat_number TEXT NOT NULL,\n                customer_name TEXT NOT NULL\n            )\n        ')
    self.connection.commit()