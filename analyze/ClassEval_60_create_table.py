def create_table(self):
    """
    Crea una tabla "tickets" en la base de datos si no existe ya. Los campos incluyen ID de tipo int, nombre de la película de tipo str, nombre del teatro de tipo str, número de asiento de tipo str y nombre del cliente de tipo str.
    :return: None
    """
    cursor = self.conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            movie_name TEXT NOT NULL,
            theater_name TEXT NOT NULL,
            seat_number TEXT NOT NULL,
            customer_name TEXT NOT NULL
        )
    ''')
    self.conn.commit()