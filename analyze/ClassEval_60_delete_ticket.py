def delete_ticket(self, ticket_id):
    """
    "tickets" तालिका से टिकट ID द्वारा एक टिकट हटाता है।
    :param ticket_id: int, हटाने के लिए टिकट की ID।
    :return: None
    """
    cursor = self.conn.cursor()
    cursor.execute("DELETE FROM tickets WHERE id = ?", (ticket_id,))
    self.conn.commit()