def create_table(self):
    """
    Crea una tabella "tickets" nel database se non esiste già. I campi includono ID di tipo int, nome del film di tipo str, nome del teatro di tipo str, numero del posto di tipo str e nome del cliente di tipo str.
    :return: None
    """
    cursor = self.conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_film TEXT NOT NULL,
            nome_teatro TEXT NOT NULL,
            numero_posto TEXT NOT NULL,
            nome_cliente TEXT NOT NULL
        )
    ''')
    self.conn.commit()