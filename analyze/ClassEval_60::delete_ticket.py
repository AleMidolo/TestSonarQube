def delete_ticket(self, ticket_id):
        """
        根据票据 ID 从 "tickets" 表中删除票据。
        :param ticket_id: int, 要删除的票据的 ID。
        :return: None
        """
        self.cursor.execute('''
                DELETE FROM tickets WHERE id = ?
            ''', (ticket_id,))
        self.connection.commit()