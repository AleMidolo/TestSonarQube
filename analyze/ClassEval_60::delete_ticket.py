def delete_ticket(self, ticket_id):
    """
        Elimina un ticket dalla tabella "tickets" in base all'ID del ticket.
        :param ticket_id: int, l'ID del ticket da eliminare.
        :return: None
        """
    self.cursor.execute('\n                DELETE FROM tickets WHERE id = ?\n            ', (ticket_id,))
    self.connection.commit()