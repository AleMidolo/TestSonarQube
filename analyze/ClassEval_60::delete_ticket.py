def delete_ticket(self, ticket_id):
    """
        Elimina un ticket de la tabla "tickets" por ID de ticket.
        :param ticket_id: int, el ID del ticket a eliminar.
        :return: None
        """
    self.cursor.execute('\n                DELETE FROM tickets WHERE id = ?\n            ', (ticket_id,))
    self.connection.commit()