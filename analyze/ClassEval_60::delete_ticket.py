def delete_ticket(self, ticket_id):
    """
    Deletes a ticket from the "tickets" table by ticket ID.
    :param ticket_id: int, the ID of the ticket to delete.
    :return: None
    """
    self.cursor.execute('\n            DELETE FROM tickets WHERE id = ?\n        ', (ticket_id,))
    self.connection.commit()