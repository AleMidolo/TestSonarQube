def delete_ticket(self, ticket_id):
        """
        Deletes a ticket from the "tickets" table by ticket ID.
        :param ticket_id: int, the ID of the ticket to delete.
        :return: None
        """
        self.cursor.execute('''
                DELETE FROM tickets WHERE id = ?
            ''', (ticket_id,))
        self.connection.commit()