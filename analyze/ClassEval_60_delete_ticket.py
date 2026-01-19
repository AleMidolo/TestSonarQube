def delete_ticket(self, ticket_id):
    """
    Elimina un ticket dalla tabella "tickets" in base all'ID del ticket.
    :param ticket_id: int, l'ID del ticket da eliminare.
    :return: None
    """
    query = "DELETE FROM tickets WHERE id = %s"
    self.cursor.execute(query, (ticket_id,))
    self.connection.commit()