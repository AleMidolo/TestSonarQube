def search_tickets_by_customer(self, customer_name):
    """
    Cerca i biglietti nella tabella "tickets" per nome del cliente.
    :param customer_name: str, il nome del cliente da cercare.
    :return: lista di tuple, le righe dalla tabella "tickets" che corrispondono ai criteri di ricerca.
    >>> ticket_db = MovieTicketDB("ticket_database.db")
    >>> ticket_db.create_table()
    >>> ticket_db.insert_ticket("Movie A", "Theater 1", "A1", "John Doe")
    >>> result = ticket_db.search_tickets_by_customer("John Doe")
    len(result) = 1
    """
    self.cursor.execute('\n            SELECT * FROM tickets WHERE customer_name = ?\n        ', (customer_name,))
    return self.cursor.fetchall()