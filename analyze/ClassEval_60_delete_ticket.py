def delete_ticket(self, ticket_id):
    """
    Elimina un ticket de la tabla "tickets" por ID de ticket.
    :param ticket_id: int, el ID del ticket a eliminar.
    :return: None
    """
    cursor = self.connection.cursor()
    cursor.execute("DELETE FROM tickets WHERE id = ?", (ticket_id,))
    self.connection.commit()
    cursor.close()