def search_tickets_by_customer(self, customer_name):
    """
        Busca boletos en la tabla "tickets" por nombre de cliente.
        :param customer_name: str, el nombre del cliente a buscar.
        :return: lista de tuplas, las filas de la tabla "tickets" que coinciden con los criterios de búsqueda.
        >>> ticket_db = MovieTicketDB("ticket_database.db")
        >>> ticket_db.create_table()
        >>> ticket_db.insert_ticket("Movie A", "Theater 1", "A1", "John Doe")
        >>> result = ticket_db.search_tickets_by_customer("John Doe")
        len(result) = 1
        """
    self.cursor.execute('\n            SELECT * FROM tickets WHERE customer_name = ?\n        ', (customer_name,))
    return self.cursor.fetchall()