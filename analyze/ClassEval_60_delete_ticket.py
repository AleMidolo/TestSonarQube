def delete_ticket(self, ticket_id):
    """
        "tickets" तालिका से टिकट ID द्वारा एक टिकट हटाता है।
        :param ticket_id: int, हटाने के लिए टिकट की ID।
        :return: None
        """
    self.cursor.execute('\n                DELETE FROM tickets WHERE id = ?\n            ', (ticket_id,))
    self.connection.commit()