def delete_ticket(self, ticket_id):
    """
    Deletes a ticket from the "tickets" table by ticket ID.
    :param ticket_id: int, the ID of the ticket to delete.
    :return: None
    """
    cursor = self.connection.cursor()
    cursor.execute("DELETE FROM tickets WHERE id = ?", (ticket_id,))
    self.connection.commit()